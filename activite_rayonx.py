cap.release()

if ret == True:
    while True:

        ret, frame = cap.read()

        cv2.imshow('frame', frame)

        import numpy as np

        else:
            print("Impossible de recuperer la frame correctement !")

        if cap.isOpened():            
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

else:
    import cv2
    print("Impossible d'ouvrir la camera !")

frame = cv2.bitwise_not(frame)
cap = cv2.VideoCapture(0)