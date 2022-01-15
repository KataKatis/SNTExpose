cap.release()

if ret == True:
    while True:

        ret, frame = cap.read()

        cv2.imshow('frame', frame)

        import numpy as np

        else:
            print("Impossible de récupérer la frame correctement !")

        if cap.isOpened():            
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            

            if cv2.waitKey(1) == ord('q'):
                break

else:
    import cv2
    print("Impossible d'ouvrir la caméra !")

frame = cv2.bitwise_not(frame)
cv2.destroyAllWindows()
cap = cv2.VideoCapture(0)