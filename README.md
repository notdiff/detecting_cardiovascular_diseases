# Система выявления отклонений в работе сердечно сосудистой системы

<p>Проект был разработан для всероссиского конкурса научных работ школьников "ЮНИОР"</p>

---

#### Файлы репозитория

* [```process```](https://github.com/XXXM1R0XXX/final2/tree/b2c27b43e21dbc5ec4dfeceb6c71d734852672b9/process "перейти в папку") - папка с кодом препроцессинга данных
* [```web```](https://github.com/XXXM1R0XXX/final2/tree/dcd84f38b0393c7fe9dec1a7e1064d3fa53e2e5a/web "перейти в папку") - папка с кодом веб-сайта
* [```inference_example.ipynb```](https://github.com/XXXM1R0XXX/final2/blob/dcd84f38b0393c7fe9dec1a7e1064d3fa53e2e5a/inference_example.ipynb "перейти в файл") - пример инференса модели
* [```training_example.ipynb```](https://github.com/XXXM1R0XXX/final2/blob/dcd84f38b0393c7fe9dec1a7e1064d3fa53e2e5a/training_example.ipynb "перейти в файл") - пример обучения модели

---

##### Сторонние файлы

Собранный и обработанный датасет доступен по <a href="https://drive.google.com/file/d/1Rt0I7Svrx77tFMCsNubEQ-cDY8hD-iCk/view?usp=drive_linkk">ссылке<a/>

---
## Методы
#### 1. SMOTE - Synthetic Minority Over-sampling Technique
Это алгоритм генерации синтетических примеров, которые были бы похожи на имеющиеся в малочисленном классе, но при этом не дублировали их. Для создания новой записи используется среднее значение между записями похожими друг на друга

[![Smote](https://dataknowsall.com/hs-fs/hubfs/imbalanced.png?width=800&height=350&name=imbalanced.png)](https://dataknowsall.com/hs-fs/hubfs/imbalanced.png?width=800&height=350&name=imbalanced.png)

[![smote ecg](https://i.ibb.co/72ZsqfT/image.png)](https://i.ibb.co/72ZsqfT/image.png)

## 2. ECG Net with Squeeze-and-Excitation blocks
[![ecg net](https://i.ibb.co/dD3v41F/ecg.png "ecg net")](https://i.ibb.co/dD3v41F/ecg.png "ecg net")
---
