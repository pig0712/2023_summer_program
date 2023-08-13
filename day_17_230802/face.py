import cv2

haar_face='C:/Users/koll2/OneDrive/summer_program_2023/day_17_230802/123.xml'

haar_face='123.xml'


face_cascade = cv2.CascadeClassifier(haar_face)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Not found camera")

while True:
    ret, img = camera.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces= face_cascade.detectMultiScale(gray, scaleFactor=1.3 , minNeighbors=1, minSize=(100,100))
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imshow('img', img)
    if cv2.waitKey(25) == 27: break  # ESC키를 누르면 종료


camera.release()
cv2.destroyAllWindows()

while True:
    ret, img = camera.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces= face_cascade.detectMultiScale(gray, scaleFactor=1.3 , minNeighbors=1, ize=(100,100))
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imshow('img', img)
    if cv2.waitKey(0) == 27: break   # ESC

camera.release()
cv2.destroyAllWindows()

