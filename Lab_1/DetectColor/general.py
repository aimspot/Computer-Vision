import cv2
import config as conf
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


def openVideo():
    cap = cv2.VideoCapture(conf.file)
    return cap


def rectangle_show(frame):
    return cv2.rectangle(frame, (conf.x, conf.y), (conf.x + conf.w_r, conf.y + conf.h_r), conf.color, conf.thickness)


def detection_yellow(hsvFrame):
    lower_yellow = np.array(conf.l_yellow, dtype=np.uint8)
    upper_yellow= np.array(conf.u_yellow, dtype=np.uint8)
    # найдите цвета в пределах указанных границ
    # маска
    yellow_mask = cv2.inRange(hsvFrame, lower_yellow, upper_yellow)
    frame_white = cv2.bitwise_and(hsvFrame, hsvFrame, mask=yellow_mask)
    return np.unique(frame_white).size

def detection_red(hsvFrame):
    lower_red = np.array(conf.l_red, np.uint8)
    upper_red = np.array(conf.u_red, np.uint8)
    red_mask = cv2.inRange(hsvFrame, lower_red, upper_red)
    frame_red = cv2.bitwise_and(hsvFrame, hsvFrame, mask=red_mask)
    return np.unique(frame_red).size

def detection_blue(hsvFrame):
    lower_blue = np.array(conf.l_blue, np.uint8)
    upper_blue = np.array(conf.u_blue, np.uint8)
    blue_mask = cv2.inRange(hsvFrame, lower_blue, upper_blue)
    frame_blue = cv2.bitwise_and(hsvFrame, hsvFrame, mask=blue_mask)
    return np.unique(frame_blue).size


def isEqual(x):
    return np.allclose(x, x[0]) # все элементы равны первому

def detection_color(hsvFrame):
    color = "Unknown"
    num_colors = [detection_yellow(hsvFrame), detection_red(hsvFrame), detection_blue(hsvFrame)]
    index_color = num_colors.index(max(num_colors))
    if isEqual(num_colors):
        return color
    else:
        color = "Yellow" if index_color == 0 else "Red" if index_color == 1 else "Blue"
    return color
