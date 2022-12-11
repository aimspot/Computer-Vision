import cv2
import cv2.gapi
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from time import sleep
from pynput import keyboard
from pynput.keyboard import Controller

class Key():
    def __init__(self, position, text, w = 90, h = 90):
        self.x, self.y = position
        self.text = text
        self.w = w
        self.h = h
        self.color = (0, 0, 255)

    def draw(self, frame):
        cvzone.cornerRect(frame, (self.x, self.y, self.w, self.h), 20, rt = 0)
        cv2.rectangle(frame, (self.x, self.y), (self.x + self.w, self.y + self.h), self.color, cv2.FILLED)  # filled заливает
        cv2.putText(frame, self.text, (self.x + 19, self.y + 57), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)



def createKeybord(position, up = False):
    x, y = position
    old_x = x
    letter_up = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "+"],
                ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'"],
                ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
                [" "]]

    letter_low = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "+"],
                ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "{", "}"],
                ["a", "s", "d", "f", "g", "h", "j", "k", "l", ":", '"'],
                ["z", "x", "c", "v", "b", "n", "m", "<", ">", "?"],
                [" "]]
    buttons = []
    for i in range(len(letter_up)):
        for j, key in enumerate(letter_up[i]):
            if up and letter_up[i][j] != " ":
                buttons.append(Key((x, y), letter_up[i][j]))
            else:
                if letter_up[i][j] == " " or letter_low[i][j] == " ":
                    buttons.append(Key((x, y), letter_low[i][j], 300, 90))
                else:
                    buttons.append(Key((x, y), letter_low[i][j]))

            x += 95
        y += 95
        x = old_x
    return buttons



def drawKeyboard(frame, keybord):
    img_new = np.zeros_like(frame, np.uint8)
    for i in keybord:
        i.draw(img_new)
    out = frame.copy()
    mask = img_new.astype(bool)
    out[mask] = cv2.addWeighted(frame, 0.7, img_new, 1 - 0.5, 0)[mask]
    return out

def drawButtonSelected(x, y, w, h, text, frame, color):
    cv2.rectangle(frame, (x, y), (x + w, y + h), color,
                  cv2.FILLED)
    cv2.putText(frame, text, (x + 19, y + 57), cv2.FONT_HERSHEY_PLAIN, 4,
                (255, 255, 255), 5)





def start():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    text = ""

    detector = HandDetector(detectionCon=0.5)
    flag = False
    buttons = createKeybord((20, 20), flag)
    keybordCon = Controller()


    while True:
        succes, frame = cap.read()
        frame = detector.findHands(frame)
        hands, bbox = detector.findPosition(frame)

        #keyboard
        frame = drawKeyboard(frame, buttons)

        #check hands
        if hands:
            for button in buttons:
                x, y = button.x, button.y
                w, h = button.w, button.h

                if x < hands[8][0] < x + w and y< hands[8][1] <y + h: # 8 указательный палец, 0 x координата
                    drawButtonSelected(x, y, w, h, button.text, frame, (0, 0, 255))
                    # если дистанция между двумя пальцами 8 и 12 очень маленькая < 60

                    l, _, _ = detector.findDistance(8, 12, frame)
                    change_l, _, _ = detector.findDistance(4, 20, frame)
                    delete_l, _, _ = detector.findDistance(4, 13, frame)
                    enter_l, _, _ = detector.findDistance(4, 16, frame)


                    if l < 50:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0),
                                      cv2.FILLED)
                        cv2.putText(frame, button.text, (x + 19, y + 57), cv2.FONT_HERSHEY_PLAIN, 4,
                                    (255, 255, 255), 5)
                        keybordCon.press(button.text)
                        text += ''.join(button.text)
                        sleep(0.2)

                    if change_l < 90:
                        if flag:
                            flag = False
                        else:
                            flag = True
                        buttons = createKeybord((20, 20), flag)
                        sleep(0.25)

                    if delete_l < 30:
                        keybordCon.press(keyboard.Key.backspace)
                        text = text[:-1]
                        sleep(0.25)
                    if enter_l < 25:
                        keybordCon.press(keyboard.Key.enter)
                        text = ""





             #Вывод текста
        # cv2.rectangle(frame, (50, 600), (50 + 400, 600 + 100), (0, 0, 255),
        #               cv2.FILLED)  # filled заливает
        cv2.putText(frame, text, (50 + 19, 600 + 57), cv2.FONT_HERSHEY_PLAIN, 4,
                    (255, 255, 255), 5)



        cv2.imshow("Frame", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    start()

