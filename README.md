# Предиктивная аналитика

## Метрики

**F1**
| Model                       | CONV-AE | LSTM-AE | LSTM-VAE |
|-----------------------------|---------|---------|-------|
| Original data               |   0.78  |   0.76  |  0.73 |
| + Synthetic data (GAN's)    |     -   |   -     |   -   |
| + Synthetic data (Modelica) |   0.62  |  0.57   |   0.51|


**FAR**
| Model                       | CONV-AE | LSTM-AE | LSTM-VAE |
|-----------------------------|---------|---------|----------|
| Original data               |   8.16  |   9.29  |  4.68    |

**MAR**
| Model                       | CONV-AE | LSTM-AE | LSTM-VAE |
|-----------------------------|---------|---------|----------|
| Original data               |   28    |   31.16 |  37      |


Для синтетических данных в силу неполной физической модели (отсутствие двигателя и некоторых датчиков) использовались в качестве недостающих данных средние с дисперсным шумом.


## Основная цель кейса
Разработать программное обеспечение на основе подхода AI/ML для предсказания выхода из строя отдельных компонент авиационных систем.
**Задачи кейса:**
* Задача 1: На основе данных об отказах авиационных двигателей NASA PCoE выбрать и обучить модель машинного обучения, предсказывающую выход двигателя из строя и аномалии в сигналах от сенсоров.
* Задача 2: Получить приближенную модель физического процесса, симулирующую показания датчиков в двигателе в Open Modelica и экспортировать эту модель в FMU модуль.
* Задача 3: Разработать генератор синтетических данных на основе полученного FMU модуля.
* Задача 4: Сгененрировать синтетическую обучающую выборку и обучить на ней ранее выбранную модель машинного обучения.
* Задача 5: Произвести сравнения метрик качества двух моделей и на основе результатов предложить методику использования синтетических данных с FMU модулей для задач предиктивной аналитики.
* Задача 6: Предложить архитектуру внедрения подхода с FMU модулями в процесс эксплуатации авиационных систем. 

**Датасет:**

- Датасет Skoltech test data (SKAB) по сигналам датчиков на макете гидравлической системы;
![alt text](https://github.com/waico/SKAB/blob/master/docs/pictures/testbed.png?raw=true)
1,2 - электромагнитный клапан; 3 - резервуар с водой; 4 - водяной насос; 5 - кнопка аварийной остановки; 6 - электродвигатель; 7 - инвертор; 8 - CompactRIO; 9 - механический рычаг для смещения вала. Не показаны детали - датчик вибрации (2 штуки); измеритель давления; расходомер; термопара.

## Элементы решения:
- [X] Обученная модель машинного обучения, строящая предсказания в для сигналов технической системы [(Идеология обучения)](https://github.com/addicted-by/predictive_analysis/blob/main/notebooks/README.md):
  - [LSTM-AE](https://github.com/addicted-by/predictive_analysis/blob/main/notebooks/LSTM-AE.ipynb)
  - [Conv-AE](https://github.com/addicted-by/predictive_analysis/blob/main/notebooks/Conv_AE.ipynb)
  - [LSTM-VAE](https://github.com/addicted-by/predictive_analysis/blob/main/notebooks/LSTM-VAE.ipynb)
- [X] [Модуль для чтения и запуска FMU модуля](https://github.com/addicted-by/predictive_analysis/tree/main/generator_modelica);
- [X] Наличие генератора синтетических данных:
  - [GANS](https://github.com/addicted-by/predictive_analysis/blob/main/gan_gen.ipynb);
  - [Инженерная модель](https://github.com/addicted-by/predictive_analysis/tree/main/generator_modelica); 
- [X] Наличие метода сравнение синтетических и реальных данных (CLEARML);
- [X] [Разработанная концепция применения FMU модулей](https://github.com/addicted-by/predictive_analysis/blob/main/generated_by_gans/README.md).


## References:
- [Датасет + Аналитика](https://www.kaggle.com/datasets/yuriykatser/skoltech-anomaly-benchmark-skab/code)
- [Работа с временными рядами](https://github.com/timeseriesAI/tsai)
- [SKAB](https://github.com/waico/SKAB)
