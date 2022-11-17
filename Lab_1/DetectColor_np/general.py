import cv2
import conf
import keyboard
import numpy as np


def keybordCatch(cap):
    if keyboard.is_pressed("down") and conf.y != (cap.get(4) - conf.h_r):
        conf.y = conf.y + conf.const
        conf.h = conf.h + conf.const
    if keyboard.is_pressed("up") and conf.y != 0:
        conf.y = conf.y - conf.const
        conf.h = conf.h - conf.const
    if keyboard.is_pressed("left") and conf.x != 0:
        conf.x = conf.x - conf.const
        conf.w = conf.w - conf.const
    if keyboard.is_pressed("right") and conf.x != (cap.get(3) - conf.w_r):
        conf.x = conf.x + conf.const
        conf.w = conf.w + conf.const


def rectangle_show(frame):
    return cv2.rectangle(frame, (conf.x, conf.y), (conf.x + conf.w_r, conf.y + conf.h_r), conf.color, conf.thickness)

def openVideo():
    return cv2.VideoCapture(conf.file)

def check_color(pixel):
    if (conf.l_yellow < pixel).all() and (pixel < conf.u_yellow).all():
        return 1
    if (conf.l_red < pixel).all() and (pixel < conf.u_red).all():
        return 2
    if (conf.l_blue < pixel).all() and (pixel < conf.u_blue).all():
        return 3
    else:
        return 0


def detectionColor(hsvFrame):
    #print(hsvFrame)
    colors = []
    height, width, channels = hsvFrame.shape
    #print(height)
    #print(width)
    for w in range(0, width):
        for h in range(0, height):
            colors.append(check_color(np.array(hsvFrame[h, w])))
    #print(colors)
    index_color = np.argmax(np.bincount(np.array(colors)))
    print(index_color)
    color = "Yellow" if index_color == 1 else "Red" if index_color == 2 else "Blue" if index_color == 3 else "Unknown"
    return color


    # a = np.array([1, 1, 1])
    # b = np.array([2, 4, 2])
    # c = np.array([3, 3, 3])
    # if (a < b).all() and (b < c).all():
    #     print("True")
    # else:
    #     print("False")
