from PyQt5 import QtWidgets
from function import face_detection
import cv2

frame = cv2.VideoCapture(0)

windows = QtWidgets.QApplication([])


face_detection.face_detection()
def main():
    tickmark = cv2.getTickCount()
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - tickmark)
    test = cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow('video', frame)

    fenetre = Tk()

    champ_label = Label(fenetre, text="hello world")
    bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)

    champ_label.pack()
    bouton_quitter.pack()
    # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
    fenetre.mainloop()




