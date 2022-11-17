import general
import cv2
import conf


def start():
    cap = general.openVideo()
    while (cap.isOpened()):
        ret, frame = cap.read()
        if frame is None:
            break
        Frame = cv2.cvtColor(frame[conf.y: conf.h, conf.x:conf.w], cv2.COLOR_BGR2HSV)

        general.keybordCatch(cap)
        general.rectangle_show(frame)

        cv2.putText(frame, general.detectionColor(Frame), (conf.x + 60, conf.y + conf.h_r - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, conf.color, 2)

        cv2.imshow('Asap', frame)
        cv2.imshow('Asap_2', Frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    start()
