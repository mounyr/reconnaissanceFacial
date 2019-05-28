import cv2
import function.parameters as c

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
cap = cv2.VideoCapture(0)
width = int(cap.get(3))
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    tab_face = []
    tickmark = cv2.getTickCount()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=4, minSize=(10, 10))
    for x, y, w, h in face:
        tab_face.append([x, y, x+w, y+h])
    index = 0
    for x, y, x2, y2 in tab_face:
        if not index or (x-tab_face[index-1][0] > c.marge or y-tab_face[index-1][1] > c.marge):
            if x <= 90:
                color = c.color_gauche
            elif x >= 300:
                color = c.color_droite
            else:
                color = c.color_centre
            cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, str(x), (x, y), font, 1, color, 2, cv2.LINE_AA)
        index += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow('video', frame)
cap.release()
cv2.destroyAllWindows()
