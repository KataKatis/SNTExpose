# Capture properties : https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html
# Color Space Conversion : https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html#color_convert_rgb_gray
# Color conversions : https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html#color_convert_rgb_gray

import cv2
import numpy as np

CHARACTERS_LIST = " .,:!=+%@" # caracteres ascii


def ascii(src, lignes=64, colonnes=260):
    resultat = "" # chaine de caractere ascii affichee dans le terminal
    hauteur, largeur = frame.shape # proprietes de l'image
    cell_height = hauteur / lignes # nombre de pixels en hauteur pour une case
    cell_width = largeur / colonnes # nombre de pixels en largeur pour une case

    for y in range(lignes):
        for x in range(colonnes):
            depy, arry, depx, arrx = int(cell_height*y), int(cell_height*(y+1)), int(cell_width*x), int(cell_width*(x+1))
            moyenne = int(np.mean(frame[depy:arry, depx:arrx])) # moyenne de gris pour un groupe de pixels
            char = CHARACTERS_LIST[int(moyenne/(255/len(CHARACTERS_LIST))-0.1)] # determine le caractere a ajouter en fonction de la moyenne de gris
            resultat += char
        resultat += "\n"
    return resultat # retourne la chaine de caractere ascii



cap = cv2.VideoCapture(0) # acceder a la webcam

if cap.isOpened(): # si on arrive a acceder a la webcam
    while True:
        ret, frame = cap.read() # ret = True/False (si la frame est correcte) et frame -> numpy array

        if ret == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # videocapture en noir et blanc

            print(ascii(frame)) # afficher dans le terminal les caracteres ascii

            if cv2.waitKey(1) == ord('q'): # 50 ms --> 20 fps
                break

        else: # si la frame ne peut pas etre recuperer
            print("Can't recuperate frame correctly !")

else: # si cap.isOpened renvoie False
    print("Cannot open camera")


cap.release()
cv2.destroyAllWindows()