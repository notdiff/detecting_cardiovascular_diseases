# Система выявления отклонений в работе сердечно сосудистой системы

<p>Проект был разработан для всероссиского конкурса научных работ школьников "ЮНИОР"</p>

---

#### Файлы репозитория

<ul>
  <li>
    [```src/utils.py```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/affda0c023356fe89cb821b88f65bcd060583893/src/utils.py "перейти к файлу")  - файл функций подсчета метрик и цикла обучения и т.д.</li>
  <li>
    src/model.py - ахитектура модели EcgNet с squeeze and excitation блоками</li>
  <li>
    process/SMOTE.ipynb - реализация алгоритма SMOTE для ЭКГ сигналов</li>
  <li>
    process/process_ptbxl.ipynb - обработка оригинального датасета</li>
  <li>
    process/r_peaks_process.ipynb - расширение данных за счет смены представления, выделение QRS комплекса</li>
  <li>
    train.ipynb - ноутбук с полным пайплайном обучения</li>
  <li>
    inference_example.ipynb - ноутбук с примером инференса системы обученных моделей</li>
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

[![Smote](https://dataknowsall.com/hs-fs/hubfs/imbalanced.png?width=800&height=350&name=imbalanced.png)](https://dataknowsall.com/hs-fs/hubfs/imbalanced.png?width=800&height=350&name=imbalanced.png)

[![smote ecg](https://i.ibb.co/72ZsqfT/image.png)](https://i.ibb.co/72ZsqfT/image.png)

## 2. ECG Net with Squeeze-and-Excitation blocks
[![ecg net](https://i.ibb.co/dD3v41F/ecg.png "ecg net")](https://i.ibb.co/dD3v41F/ecg.png "ecg net")
---
