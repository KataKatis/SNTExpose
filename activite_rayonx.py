cap.release()  # arrete d'acceder a la camera

if ret == True:  # si la frame a bien ete recuperee
    while True:

        ret, frame = cap.read()  # recupere la frame

        cv2.imshow('frame', frame)  # afficher l'image

        import numpy as np

        else:  # si la frame ne peut pas etre recuperee
            print("Impossible de recuperer la frame correctement !")

        if cap.isOpened():  # si on arrive a acceder a la webcam          
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # frame en noir et blanc

else:  # si on arrive pas à acceder a la webcam
    import cv2
    print("Impossible d'ouvrir la camera !")

frame = cv2.bitwise_not(frame)  # renvoie le negatif de la frame
cap = cv2.VideoCapture(0)  # acceder a la webcam