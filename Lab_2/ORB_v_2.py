import numpy as np
import cv2

def findValue(out, max_x, max_y, min_x, min_y):
    start_point = (int(min_x), int(min_y))

    end_point = (int(max_x), int(max_y))

    color = (0, 255, 0)

    thickness = 2

    return cv2.rectangle(out, start_point, end_point, color, thickness)

def drawMatches(img1, kp1, img2, kp2, matches):
    #Cоздаём общее изображение
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]
    out = np.zeros((max([rows1,rows2]), cols1+cols2, 3), dtype='uint8')
    # query изображение слева
    out[:rows1,:cols1] = np.dstack([img1, img1, img1])
    #  train справа от него
    out[:rows2,cols1:] = np.dstack([img2, img2, img2])
    max_x = max_y = min_x = min_y = 0
    for mat in matches:

        # Находим соответсвующие точки
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx


        # x - columns
        # y - rows

        (x1, y1) = kp1[img1_idx].pt
        (x2, y2) = kp2[img2_idx].pt
        print(f'IMG_1{(x1, y1)}')
        print(f'IMG_2{(x2, y2)}')
        if min_x == 0 and min_y == 0:
            min_x = x1
            min_y = y1
        if max_x < x1:
            max_x = x1
        if min_x > x1:
            min_x = x1
        if max_y < y1:
            max_y = y1
        if min_y > y1:
            min_y = y1


        cv2.circle(out, (int(x1),int(y1)), 4, (255, 0, 0), 1)
        cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (255, 0, 0), 1)

        cv2.line(out, (int(x1),int(y1)), (int(x2)+cols1,int(y2)), (255, 0, 0), 1)

    # Show the image
    findValue(out, max_x, max_y, min_x, min_y)
    cv2.imshow('Matched Features', out)
    cv2.waitKey(0)
    cv2.destroyWindow('Matched Features')


    # Also return the image if you'd like a copy
    return out

img1 = cv2.imread('data/example_5/2.jpg',0)
img2 = cv2.imread('data/example_5/1.jpg',0)

# инициализируем ORB
orb = cv2.ORB_create()

# Теперь определим ключевые точки и вычислим дескрипторы для изображений
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Сопоставляем точки
matches = bf.match(des2, des1)

#Отсортируйте их в порядке их удаленности.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = drawMatches(img1, kp1, img2, kp2, matches[:20])

cv2.imshow('dst', img3)
