import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
cap = cv2.VideoCapture(0)
width = int(cap.get(3))
marge = 80
index = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.6, minNeighbors=8)
    for x, y, w, h in face:
        cv2.imwrite('./../photos/victor/img-{:d}.png'.format(index), frame[y:y+h, x:x+w])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        index += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('video', frame)
cap.release()
cv2.destroyAllWindows()