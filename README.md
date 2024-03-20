# Система выявления отклонений в работе сердечно сосудистой системы

<p>Проект был разработан для всероссиского конкурса научных работ школьников "ЮНИОР"</p>

---

#### Файлы репозитория

* [```scr/utils.py```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/affda0c023356fe89cb821b88f65bcd060583893/src/utils.py "перейти в файл") - файл функций подсчета метрик и цикла обучения и т.д.
* [```src/ecg_net.py```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/d17a19be4365baef4e2a907001a305b1003bd5a0/src/ecg_net.py "перейти в файл") - ахитектура модели EcgNet с squeeze and excitation блоками
* [```process/SMOTE.ipynb```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/d17a19be4365baef4e2a907001a305b1003bd5a0/process/SMOTE.ipynb "перейти в файл") - реализация алгоритма SMOTE для ЭКГ сигналов
* [```process/process_ptbxl.ipynb```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/d17a19be4365baef4e2a907001a305b1003bd5a0/process/process_ptbxl.ipynb "перейти в файл") - обработка оригинального датасета
* [```process/r_peaks_process.ipynb```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/d17a19be4365baef4e2a907001a305b1003bd5a0/process/r_peaks_process.ipynb "перейти в файл") - расширение данных за счет смены представления, выделение QRS комплекса
* [```inference_example.ipynb```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/d17a19be4365baef4e2a907001a305b1003bd5a0/inference_example.ipynb "перейти в файл") - пример инференса модели
* [```train.ipynb```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/d17a19be4365baef4e2a907001a305b1003bd5a0/train.ipynb "перейти в файл") - ноутбук с полным пайплайном обучения
* [```web```](https://github.com/notdiff/detecting_cardiovascular_diseases/tree/8bc9c58fab05614232012dbb04ee1cc36f547fa3/web "перейти в папку") - web демо проекта (beta)
* [```requirements.txt```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/b4b18b6f28dbbb0ec07639dd8ca72a52e7126037/requirements.txt "перейти в папку") - файл зависимостей (только для тех.части проекта)

---

#### Сторонние файлы

Собранный и обработанный датасет доступен по <a href="https://drive.google.com/file/d/1Rt0I7Svrx77tFMCsNubEQ-cDY8hD-iCk/view?usp=drive_linkk">ссылке<a/> (размер около 10ГБ)  <br/>
Архив моделей можно получить <a href="http://site.m1r0.webtm.ru:8080/s/ex6dKfgaEqLRJpg/download/models.zip">здесь<a/> (размер около 1ГБ)

---
## Методы
#### 1. SMOTE - Synthetic Minority Over-sampling Technique
Это алгоритм генерации синтетических примеров, которые были бы похожи на имеющиеся в малочисленном классе, но при этом не дублировали их. Для создания новой записи используется среднее значение между записями похожими друг на друга

[![Smote](https://dataknowsall.com/hs-fs/hubfs/imbalanced.png?width=800&height=350&name=imbalanced.png)](https://dataknowsall.com/hs-fs/hubfs/imbalanced.png?width=800&height=350&name=imbalanced.png)

[![smote ecg](https://i.ibb.co/72ZsqfT/image.png)](https://i.ibb.co/72ZsqfT/image.png)

## 2. ECG Net with Squeeze-and-Excitation blocks
[![ecg net](https://i.ibb.co/dD3v41F/ecg.png "ecg net")](https://i.ibb.co/dD3v41F/ecg.png "ecg net")
---
