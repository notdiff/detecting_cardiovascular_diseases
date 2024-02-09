# Система выявления отклонений в работе сердечно сосудистой системы

<p>Проект был разработан для всероссиского конкурса научных работ школьников "ЮНИОР"</p>

---

#### Файлы репозитория

<ul>
  <li>
    src/utils.py  - файл функций подсчета метрик и цикла обучения и т.д.</li>
  <li>
    src/model.py - ахитектура модели EcgNet с squeeze and excitation блоками</li>
  <li>
    train.ipynb - ноутбук с полным пайплайном обучения</li>
  <li>
    requirements.txt - зависимости необходимые для работы</li>
</ul>

---

##### Сторонние файлы

Собранный и обработанный датасет доступен по <a href="https://drive.google.com/file/d/1Rt0I7Svrx77tFMCsNubEQ-cDY8hD-iCk/view?usp=drive_linkk">ссылке<a/>

---
## Методы
#### 1. SMOTE - Synthetic Minority Over-sampling Technique
Это алгоритм генерации синтетических примеров, которые были бы похожи на имеющиеся в малочисленном классе, но при этом не дублировали их. Для создания новой записи используется среднее значение между записями похожими друг на друга
[![Smote](https://www.dataknowsall.com/images/posts/imbalanced.png "Smote")](https://www.dataknowsall.com/images/posts/imbalanced.png "Smote")

[![smote ecg](https://i.ibb.co/72ZsqfT/image.png "smote ecg")](https://i.ibb.co/72ZsqfT/image.png "smote ecg")

## 2. ECG Net with Squeeze-and-Excitation blocks
[![ecg net](https://i.ibb.co/dD3v41F/ecg.png "ecg net")](https://i.ibb.co/dD3v41F/ecg.png "ecg net")
---
