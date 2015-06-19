picMatrix
=========

le FriendMatrix
```
Короче, делаем вот такую штуку http://friendmatrix.co/
На входе: Много картинок, каждая из которых имеет положительный вес
На выходе: одна картинка, в которую включены все входные картинки, и чем больше вес картинки, тем у нее размер больше
```

для работы с изображениями будем навреное использовать http://effbot.org/zone/pil-index.htm

На какие части можно разделить задачу?

0. определить в какую матрицу мы можем поместить наши картинки
1. Округление весов 
2. Определение местоположения каждой входной картины в результирующей картинке
3. Работа с непосредственно с рендерингом изображения: уменьшение, обрезка, вставка на соответствующее место и тп

Что такое округление весов? это:
результирующая картинка состоит из квадратных ячеек
```
____________________
|__|__|__|__|__|__|__|__|
|__|__|__|__|__|__|__|__|
|__|__|__|__|__|__|__|__|
|__|__|__|__|__|__|__|__|
|__|__|__|__|__|__|__|__|
|__|__|__|__|__|__|__|__|
|__|__|__|__|__|__|__|__|
|__|__|__|__|__|__|__|__|
```

Давайте вначале он всегда будет квадратным


