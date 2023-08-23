# neural-SER

Speech emotion recognition using convolutional neural networks

1. Описание задачи
2. Описание решения
3. Результат

## Описание задачи

Использовать четыре распространённых датасета:

- [Toronto emotional speech set (TESS)](https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess)
- [Surrey Audio-Visual Expressed Emotion (SAVEE)](https://www.kaggle.com/datasets/ejlok1/surrey-audiovisual-expressed-emotion-savee)
- [Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS)](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)
- [Crowd Sourced Emotional Multimodal Actors Dataset (CREMA-D)](https://www.kaggle.com/datasets/ejlok1/cremad)

Распознать шесть базовых эмоций по Экману:

- anger
- disgust
- fear
- happiness
- neutral
- sadness
- surprise
  
С использованием пяти моделей свёрточных нейронных сетей:

- VGG19
- Xception
- InceptionV3
- ResNet101V2
- DenseNet201

Расчитать метрики точности классификации:

- accuracy
- precision
- recall
- f1-score

## Описание решения

Зависимости:

- pandas
- numpy
- matplotlib
- tensorflow v2
- scikit-learn
- seaborn

`preprocess_data.ipynb` - составление csv таблиц с путями до файлов и эмоциями

`modeling.ipynb` - обучение моделей, визуализация истории обучения, расчёт метрик, проверка обучения моделей на тестовом наборе
