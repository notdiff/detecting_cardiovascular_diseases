import torch
from torch.utils.data import Dataset

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def calculate_accuracy(output, target):
    train_accuracy = torch.sum(target == output) / len(target)
    return train_accuracy


def calculate_f1(preds, labels):
    tp = torch.sum(preds[labels == preds] == 1)
    preds_p = torch.sum(preds == 1)
    labels_p = torch.sum(labels == 1)
    recall = (tp / labels_p if labels_p != 0 else 0)
    precision = (tp / preds_p if preds_p != 0 else 0)
    if recall + precision == 0: return 0
    return (2 * recall * precision) / (recall + precision)


class MetricMonitor:
    def __init__(self, float_precision=3):
        self.float_precision = float_precision
        self.reset()

    def reset(self):
        self.metrics = defaultdict(lambda: {"val": 0, "count": 0, "avg": 0})

    def update(self, metric_name, val):
        metric = self.metrics[metric_name]

        metric["val"] += val
        metric["count"] += 1
        metric["avg"] = metric["val"] / metric["count"]

    def __str__(self):
        return " | ".join(
            [
                "{metric_name}: {avg:.{float_precision}f}".format(
                    metric_name=metric_name, avg=metric["avg"], float_precision=self.float_precision
                )
                for (metric_name, metric) in self.metrics.items()
            ]
        )


class EcgPTBDataset(Dataset):
    def __init__(self, labels, path='/'):
        self.x_paths = [labels.iloc[i, 0] for i in range(len(labels))]
        self.labels = [labels.iloc[i, 1] for i in range(len(labels))]
        self.path = path

    def __len__(self):
        return len(self.x_paths)

    def __getitem__(self, idx):

        hr = torch.tensor(np.load(self.path + self.x_paths[idx] + '.npy'))[None, :, :]

        target = self.labels[idx]

        return hr, target


def train(model, loss_fn, scheduler, optimizer, n_epoch=3, device='cuda'):
    train_losses = []
    val_losses = []
    train_acc = []
    val_acc = []
    val_f1 = []

    max_f1 = 0

    val_accuracy, val_loss, val_f1_score = evaluate(model, val_loader, loss_fn=loss_fn, device=device)
    wandb.log({"F1": val_f1_score, "Acc": val_accuracy, 'loss': val_loss})

    for epoch in range(n_epoch):
        print("Epoch:", epoch+1)

        model = model.train()
        for batch in tqdm(train_loader):
            X_batch, y_batch = batch
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)

            logits = model(X_batch.float())

            logits = torch.nn.functional.softmax(logits, dim=1)

            loss = loss_fn(logits, y_batch.to(torch.int64))

            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            train_losses.append(loss.item())

            model_answers = torch.argmax(logits, dim=1).to(torch.int64)

            train_accuracy = torch.sum(y_batch == model_answers) / len(y_batch)
            train_acc.append(train_accuracy.item())


        model.eval()

        val_accuracy, val_loss, val_f1_score = evaluate(model, val_loader, loss_fn=loss_fn, device=device)
        wandb.log({"F1": val_f1_score, "Acc": val_accuracy, 'loss': val_loss})
        clear_output(wait=True)

        if  max_f1 < val_f1_score:
            pass
            torch.save(model.state_dict(), f'/content/drive/MyDrive/models/ecgNet_f1:{val_f1_score:.4f}.pth')

        val_losses.append(val_loss.item())
        val_acc.append(val_accuracy)

        scheduler.step(val_loss)


def evaluate(model, dataloader, loss_fn, device):
    losses = []
    num_correct = 0
    num_elements = 0
    f1 = torchmetrics.F1Score(num_classes=2)
    f1_score = 0

    model = model.eval()
    for batch in tqdm(dataloader):
        X_batch, y_batch = batch
        X_batch, y_batch = X_batch.to(device), y_batch.to(device).float()

        with torch.no_grad():
            logits = model(X_batch.float())

            logits = torch.nn.functional.softmax(logits, dim=1)

            loss = loss_fn(logits, y_batch.to(torch.int64))
            losses.append(loss.item())

            y_pred = torch.argmax(logits, dim=1).to(torch.int64)

            f1_score += f1(y_pred.cpu(), y_batch.cpu())

            num_elements += len(y_batch)
            num_correct += torch.sum(y_pred == y_batch)

    accuracy = num_correct / num_elements
    f1_score = f1_score / len(dataloader)

    return accuracy.item(), np.mean(losses), f1_score.item()