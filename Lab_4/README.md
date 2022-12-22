# Computer-Vision
## Теоретическая справка
Данная работа включает в себя использования следующих библеотек:
* CVzone
* Mediapipe
* Pynput.keyboard
Данные библеотеки позволяют нам обнаружать руку и ключевые точки на ней.
### Функция findDistance:
```
detector = HandDetector(detectionCon=0.5)
detector.findDistance
```
Поиск расстояния между двумя точками в 2D пространстве.
```
return:  lenght,  info (x1,y1,x2,y2,cx,cy), img
```
### Функция findPosition:
```
detector = HandDetector(detectionCon=0.5)
detector.findPosition(frame)
```
Получение контрольных точек и bounding box руки.

### Функция findHands:
```
detector = HandDetector(detectionCon=0.5)
detector.findHands(frame)
```
Получение контрольных точек и bounding box руки.


## Принцип работы можно представить следующим образом:
![image](https://user-images.githubusercontent.com/82668230/209147364-30d46a8e-c444-444c-9c89-b8aab8ab2fe2.png)
