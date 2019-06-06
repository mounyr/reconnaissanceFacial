#!/usr/bin/env python
import cv2
import pickle
import numpy as np
import function.parameters as c

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./trainner.yml")


with open("./labels.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    tickmark = cv2.getTickCount()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=2, minSize=(150, 150))
    for (x, y, w, h) in faces:
        roi_gray = cv2.resize(gray[y:y+h, x:x+w], (c.min_size, c.min_size))
        id_, conf = recognizer.predict(roi_gray)
        if conf <= 125:
             color = c.color_droite
             name = labels[id_]
        else:
            color = c.color_centre
            name = "Inconnu"

        label = name+" "+'{:5.2f}'.format(conf)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_DUPLEX, 1, c.color_centre, 1, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, c.color_centre, 2)
    cv2.imshow('tes', frame)
    key=cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('a'):
        for cpt in range(100):
            ret, frame = cap.read()

cv2.destroyAllWindows()
print("Fin")
