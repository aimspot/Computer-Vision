import numpy as np
import cv2


# читаем картиночки
query_img = cv2.imread("data/example_1/2.jpg")
train_img = cv2.imread("data/example_1/1.jpg")

# Конвертим в серый
query_img_bw = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)

# инициализируем ORB
orb = cv2.ORB_create()

# Теперь опредеKBV ключевые точки и вычислим
# дескрипторы для изображения запроса и трейн
queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw, None)
trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw, None)

# Сопоставляем точки
matcher = cv2.BFMatcher()
matches = matcher.match(queryDescriptors, trainDescriptors)


# Выводим финальное изображение
final_img = cv2.drawMatches(query_img, queryKeypoints,
                            train_img, trainKeypoints, matches[:5], None)

final_img = cv2.resize(final_img, (1000, 650))


cv2.imshow("Matches", final_img)
cv2.waitKey(0)
