import numpy as np
import imutils
import cv2


# подгружаем изображения
main = cv2.imread("data/example/panda.jpg")
template = cv2.imread("data/example/panda_tem.jpg")
(templateHeight, templateWidth) = template.shape[:2]

# ищем template на основном изображении
result = cv2.matchTemplate(main, template, cv2.TM_CCOEFF)



# так как после применения  matchTemplate нам возвращается одноканальная матрица  и мы используем cv2.TM_CCOEFF, нам нужно найти самую яркую точку

(_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)


topLeft = maxLoc
botRight = (topLeft[0] + templateWidth, topLeft[1] + templateHeight)
roi = main[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]



mask = np.zeros(main.shape, dtype = "uint8")

# смешиваем два изображения, чтобы затемнить фон, scr1*alpha + scr2*beta + gamma

new_image = cv2.addWeighted(main, 0.5, mask, 1, 0)


# выделяем нужную нам область на изображении
new_image[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi

# display the images
cv2.imshow("Main_image", imutils.resize(new_image, height = 650))
cv2.imshow("Templete_image", template)
cv2.waitKey(0)