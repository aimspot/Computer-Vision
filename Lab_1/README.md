# Lab 1
## DetectColor
Демонстрирует способ определение цвета на видео файле с использованием стека:
 * Python;
 * OpenCV.
## DetectColor_np
Демонстрирует способ определение цвета на видео файле с использованием стека:
 * Python;
 * OpenCV (для воспроизведения видео и отрисовки ректангла);
 * Numpy (для определение преобладающего цвета).
 ## lab_1_color
 Демонстрирует способ определение цвета на видео файле с использованием стека:
 * C++;
 * OpenCV.
# Теоритическая база
1. На вход подается RGB видеофайл;
2. Отрисовываем ректангл;
3. Меняем его цветовое пространство внутри ректангла (RGB -> BRG/HSV). 
    a) R - red (красный), G - > green (зелёный), B -> blue (синий). 
    b) H - hue (тон), S - > saturation (насыщенность), V -> value (значение цвета)
4. Для каждого цвета мы фильтруем полученый кадр с помощью функции inRange(). Первый параметр — изменяемое изображение, а второй и третий — левая и правая граница пропускаемого цвета

# Результаты работы и тестирования системы

# Выводы по работе
