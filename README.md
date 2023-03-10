# Распознавание всякого на видео

Скрипт захватывает видео с вэб камеры и выделяет квадратами лица и глаза (по умолчанию), найденные в кадре. Так же
предусмотрена возможность распознавания улыбок, человеческого тела и кошачьих лиц. И есть возможность добавлять
свои элементы распознавания.

## Модуль run.py
Основной модуль скрипта.

### Блок if \_\_name__ == '\_\_main__'

Загружает параметры распознавания. Производит захват видео. Если видео поток отсутствует, то выводит в консоль
сообщение:

`Couldn't find your webcam... Sorry :c`

Преобразует изображение в градации серого, и запускает процесс распознавания.

При нажатии клавиши **q** закрывает программу.

### is_user_wants_quit

Обнаруживает нажатие клавиши **q**. Ничего не принимает. Возвращает *bool*

### show_frame

Выводит изображение в отдельном окне. Принимает объект *frame*. Ничего не возвращает.

### draw_sqare

Рисует прямоугольники на кадре по заданным координатам. Принимает кадр и цвет прямоугольника. Так же использует
координаты и размер прямоугольника из глобальной области переменных. Ничего не возвращает

### get_cascades

Загружает список каскадов из модуля config.py. Ничего не принимает. Возвращает список каскадов

## Модуль config.py
Содержит список каскадов, представляющих из себя параметры обнаружения различных объектов на видео.
