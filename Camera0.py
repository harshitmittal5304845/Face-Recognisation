import cv2

cap=cv2.VideoCapture(0)

while True:
    ret, fram = cap.read()
    cv2.imshow('video Capture',fram,)
    k=cv2.waitkey(5) & 0xff
    if k==27:
        break
cap.release()
cv2.distroyAllWindows()