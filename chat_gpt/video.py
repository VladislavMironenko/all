import cv2


cap = cv2.VideoCapture(0)


while True:
    _ ,img = cap.read()

    cv2.imshow('Testest', img)

    key = cv2.waitKey(1)

    if key == ord('q'):
        print(key)
        break

