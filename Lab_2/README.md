# Lab 2
# Теоритическая база
# Template matching
Один из основных методов по нахождению необходимого объекта на изображении. Он представляет собой пошаговое сканирование шаблоном исходного изображения, причем на каждом шаге рассчитывается либо просто измеряется степень соответствия участка изображения существующему шаблону. Когда сканирование заканчивается, на изображении выделяется область, которая соответствует шаблону в большей степени.
Cv включает в себя несколько метрик по которым происходят вычисления:
 * CV_TM_SQDIFF — сумма квадратов разниц значений пикселей;
 * CV_TM_SQDIFF_NORMED — сумма квадрат разниц цветов, отнормированная в диапазон 0..1;
 * CV_TM_CCORR — сумма поэлементных произведений шаблона и сегмента картинки;
 * CV_TM_CCORR_NORMED — сумма поэлементных произведений, отнормированное в диапазон -1..1;
 * CV_TM_CCOEFF — кросс-коррелация изображений без среднего;
 * CV_TM_CCOEFF_NORMED — кросс-корреляция между изображениями без среднего, отнормированная в -1..1 (корреляция Пирсона).

 Алгоритм действий: 
 1. Загружаем два изображения (которые нужно найти/ на котором нужно найти);
 2. Применяем функцию cv2.matchTemplate(), в нашем случаем мы используем  cv2.TM_CCOEFF;
 3. Ищем самую яркую точку при помощи cv2.minMaxLoc;
 4. Добавляем к текущей точке изначальные размеры template изображения;
 5. Выводим изображение.
 
 
 
 Результаты работы Template matching:
 
 |  Number | Example |   
|:-:|:-:|
|  1 | ![0](https://user-images.githubusercontent.com/82668230/206853680-d5d2805c-0644-4753-8e1f-b2e872ae459a.jpg)|
|  2 | ![2](https://user-images.githubusercontent.com/82668230/206853691-9f05e4ef-d954-4554-9fd7-6a30e7902cc2.jpg)|
|  3 | ![3](https://user-images.githubusercontent.com/82668230/206853700-9019c266-647c-4622-a83b-f4139183fef9.jpg)|
|  4 | ![4](https://user-images.githubusercontent.com/82668230/206853707-6905c92b-8363-46f4-bb0d-729f84dfb196.jpg)|
|  5 | ![6](https://user-images.githubusercontent.com/82668230/206853716-ae26662c-2b93-4345-bfb1-f8c31665e402.jpg)|
|  6 | ![5](https://user-images.githubusercontent.com/82668230/206853725-37ba9b61-bf5d-4b32-8ceb-858ee200e0b4.jpg)|
|  7 | ![1](https://user-images.githubusercontent.com/82668230/206853744-ff37ef65-1080-43cc-81b6-67ffe2eb80fb.jpg)|
|  8 | ![8](https://user-images.githubusercontent.com/82668230/206853769-9c698120-d6a6-4403-8e5b-64bfd948c876.jpg)|
|  9 | ![9](https://user-images.githubusercontent.com/82668230/206853780-ad16590c-24df-494a-9804-371ae3b0ecba.jpg)|
|  10 | ![10](https://user-images.githubusercontent.com/82668230/206853794-aabc3c20-049b-43c6-9d47-8c16dd13a152.jpg)|
 

 
 
![8](https://user-images.githubusercontent.com/82668230/205068167-2eaca630-3276-44bf-89b8-164106d5c59f.jpg)


# ORB
Ориентированный FAST и повернутый BRIEF (ORB) — это быстрый надежный  детектор локальных признаков, впервые представленный Ethan Rublee et al. в 2011 году и используется в задачах компьютерного зрения, таких как распознавание объектов или 3D-реконструкция. ORB использует модифицированную версию детектора ключевых точек FAST и дескриптора BRIEF.

Алгоритм работы:
1. Загружаем изображения;
2. Инициализируем ORB;
3. Определяем дискрипторы и ключевые точки;
4. Инициализируем BFMatcher;
5. Сопостовляем дискрипторы;
6. Сортируем их в порядке удалённости;
7. Визуализируем сопостовление точек и строим рамку.

 Результаты работы ORB: 
 
|  Number | Example |   
|:-:|:-:|
|  1 |  ![1](https://user-images.githubusercontent.com/82668230/206852819-f83f7a4e-e7cd-40a1-8a34-589ed427133a.jpg)|
|  2 |  ![2](https://user-images.githubusercontent.com/82668230/206852849-20606dff-854e-42f1-92ae-83f591030649.jpg)|
|  3 |  ![3](https://user-images.githubusercontent.com/82668230/206852857-ba0d9bc9-90f2-4941-ba5a-a73a246c58b0.jpg)|
|  4 |  ![4](https://user-images.githubusercontent.com/82668230/206852864-bc44cd2a-9709-4f7d-b950-46dd96bbfd09.jpg)|
|  5 |  ![5](https://user-images.githubusercontent.com/82668230/206852867-5e4e9ca6-bd6e-4366-8f23-b593b9f43afc.jpg)|
|  6 |  ![image](https://user-images.githubusercontent.com/82668230/206448905-5675403e-97c4-43e9-a4af-b67b8556f610.png)|
|  7 |   ![6](https://user-images.githubusercontent.com/82668230/206852933-96b3a82b-42a8-4339-8c25-edd01b0b3b7c.jpg)|
|  8 |   ![8](https://user-images.githubusercontent.com/82668230/206852924-8c4a0842-5730-4169-8738-503793acba1f.jpg)|
|  9 |  ![9](https://user-images.githubusercontent.com/82668230/206852914-5f35d6a7-f1c2-4f6c-890f-d3078683d391.jpg)|
|  10 |  ![10](https://user-images.githubusercontent.com/82668230/206852908-d56fb742-1914-4477-b0a6-6536f54a482f.jpg)|
 
 
 

 
 
 # Вывод
 Опробовали функции поиска изображения на основной картинке, используя Template matching и ORB.
