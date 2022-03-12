import cv2
import numpy as np


cap = cv2.VideoCapture(0)  # acceder a la webcam


if cap.isOpened():  # si on arrive a acceder a la webcam
    while True:
        ret, frame = cap.read()  # recupere la frame
        
        if ret == True:
            frame = cv2.autorotate(frame, 0)  # oriente la frame dans le bon sens
            frame = cv2.resize(frame, (750, 500))  # agrandi la frame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # frame en noir et blanc
            frame = cv2.bitwise_not(frame)  # renvoie le negatif de la frame
            cv2.imshow('frame', frame)  # afficher l'image
            
        else:
            print("Impossible de recuperer la frame correctement !")
            
else:
    print("Impposible d'acceder a la camera")