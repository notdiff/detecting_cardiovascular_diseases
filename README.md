# Система выявления отклонений в работе сердечно сосудистой системы

Проект является усовершенствованной версией решения [хакатона AI Challenge 2023](https://github.com/ALT-F4-Team/localization-of-myocardial-infarction)

## [Видео-демо](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/main/DEMO.mp4)
---

#### Файлы репозитория

* [```scr/utils.py```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/affda0c023356fe89cb821b88f65bcd060583893/src/utils.py "перейти в файл") - файл функций подсчета метрик и цикла обучения и т.д.
* [```src/ecg_net.py```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/d17a19be4365baef4e2a907001a305b1003bd5a0/src/ecg_net.py "перейти в файл") - ахитектура модели EcgNet с squeeze and excitation блоками
* [```process/SMOTE.ipynb```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/d17a19be4365baef4e2a907001a305b1003bd5a0/process/SMOTE.ipynb "перейти в файл") - реализация алгоритма SMOTE для ЭКГ сигналов
* [```process/process_ptbxl.ipynb```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/d17a19be4365baef4e2a907001a305b1003bd5a0/process/process_ptbxl.ipynb "перейти в файл") - обработка оригинального датасета
* [```process/r_peaks_process.ipynb```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/d17a19be4365baef4e2a907001a305b1003bd5a0/process/r_peaks_process.ipynb "перейти в файл") - расширение данных за счет смены представления, выделение QRS комплекса
* [```inference_example.ipynb```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/d17a19be4365baef4e2a907001a305b1003bd5a0/inference_example.ipynb "перейти в файл") - пример инференса модели
* [```train.ipynb```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/d17a19be4365baef4e2a907001a305b1003bd5a0/train.ipynb "перейти в файл") - ноутбук с полным пайплайном обучения моделей и примером создания системы на основе catboost
* [```web```](https://github.com/notdiff/detecting_cardiovascular_diseases/tree/8bc9c58fab05614232012dbb04ee1cc36f547fa3/web "перейти в папку") - web демо проекта (beta)
* [```requirements.txt```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/b4b18b6f28dbbb0ec07639dd8ca72a52e7126037/requirements.txt "перейти в файл") - файл зависимостей (только для тех.части проекта)
* [```description.txt```](https://github.com/notdiff/detecting_cardiovascular_diseases/blob/2b506b46b601df565db6d24a8063546381086321/description.txt "перейти в файл") - описание всех представленных патололгий
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

#### 2. ECG Net with Squeeze-and-Excitation blocks
Архитектура из [статьи](https://arxiv.org/pdf/2012.05510), с доказанной медицинской эффективностью
![image](https://github.com/notdiff/detecting_cardiovascular_diseases/assets/116492863/e72d1b07-eb32-44a0-a881-7358c39e927a)

#### 3. Обучение
Этот этап достаточно проблематичен, так как даже после использования SMOTE, выборка все равно имеет дисбаланс. Поэтому была применена функция ошибок, позволяющая ориентировать модель на наблюдения в которых она не уверенна:<br/>
![image](https://github.com/notdiff/detecting_cardiovascular_diseases/assets/116492863/f9d6177d-ab26-4a5d-931a-5d0ff1974dab)<br/>
Дополнительный множитель к формуле CrossEntropy, позволяет в разы увеличивать ошибку на примерах с низкой вероятностью.
#### 4. Пайплан
Итоговый пайплайн обработки записи выглядит так<br/>
    1. На вход приходит наблюдение, происходит обработка<br/>
    2. Обработанный сигнал подается в каждую из oneVSrest сетей<br/>
    3. Далее эмбеддинги подаются в обученные бустинги. В каждый из бустингов подаеются разных подмножества признаков из сети, таким образом среднее выходом этих моделей более устойчиво к переобучению<br/>
![image](https://github.com/notdiff/detecting_cardiovascular_diseases/assets/116492863/86dafdeb-6323-48ce-9799-69c65f4d0a2a)
