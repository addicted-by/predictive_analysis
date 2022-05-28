
Основано на [GitPage](https://github.com/waico/SKAB)

# Подход к обучению
- Обучить модель на первых 400 точках каждого датасета -- примерно трети общего объема. Проверить аномалии на пересечении разницей предсказанных состояний и реальных  доверительного интервала. Таким образом получим модели, на основе которых можно предсказывать аномалии разных видов. Такой подход реализован из идеологии сильного качественного различия между возможными аномалиями.

# Возможные аномалии

[valve1](https://github.com/addicted-by/predictive_analysis/tree/main/data/valve1) - Данные, полученные из экспериментов с закрытием клапана на выходе потока из насоса.

[valve2](https://github.com/addicted-by/predictive_analysis/tree/main/data/valve2) - Данные получены из экспериментов с закрытием клапана на входе потока в насос.

[other](https://github.com/addicted-by/predictive_analysis/tree/main/data/other) - Данные, полученные из других экспериментов
 - Резкое поведение дисбаланса ротора
 - Линейное поведение дисбаланса ротора
 - Ступенчатое поведение дисбаланса ротора
 - Поведение дельта-функции Дирака дисбаланса ротора
 - Экспоненциальное поведение дисбаланса ротора
 - Медленное увеличение количества воды в контуре
 - Внезапное увеличение количества воды в контуре
 - Слив воды из бака до кавитации
 - Подача двухфазного потока на вход насоса (кавитация)
 - Водоснабжение повышенной температуры

# Модели

## Convolutional Autoencoder (Conv-AE)
| [notebook](https://github.com/addicted-by/predictive_analysis/blob/main/notebooks/Conv_AE.ipynb) | [paper](https://keras.io/examples/timeseries/timeseries_anomaly_detection/) |
|-----------------------------|---------|


## LSTM Autoencoder (LSTM-AE)
Seq2Seq model
| [notebook](https://github.com/addicted-by/predictive_analysis/blob/main/notebooks/LSTM-AE.ipynb) | [paper](https://machinelearningmastery.com/lstm-autoencoders/) |
|-----------------------------|---------|


## LSTM Variational Autoencoder (LSTM-VAE)
Seq2Seq model
| [notebook](https://github.com/addicted-by/predictive_analysis/blob/main/notebooks/LSTM-VAE.ipynb) | [paper](https://arxiv.org/pdf/1511.06349.pdf) |
|-----------------------------|---------|



