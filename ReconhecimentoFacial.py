import cv2

cap = cv2.VideoCapture(0)
larg = 640
altu = 360

#Importando os modelos 
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")

while True: 
    ret,video = cap.read()
    video = cv2.flip(video, 1) #Inverte a webcam, concerta ela

    capture = cv2.resize(video, (larg,altu), fx = 0, fy = 0, interpolation= cv2.INTER_AREA) #Img da webcam
    graycapture = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)

    #Rosto
    faces = face_cascade.detectMultiScale(graycapture, 1.3, 5)
    for (x,y,w,h) in faces: #x, y, width, heigth
        cv2.rectangle(capture, (x, y), (x+w, y+h),(255, 0, 0), 2)

        roi_graycapture = graycapture[y:y+h, x:x+w] #ROI é Region Of Interesse
        roi_capture = capture[y:y+h, x:x+w]

        print(int(x+w/2), int(y+h/2))
        cv2.imshow('Reconhecimento Facial', capture)

        #Olhos
        eyes = eye_cascade.detectMultiScale(graycapture)

        for (ex,ey,ew,eh) in eyes: #x, y, width, heigth
            cv2.rectangle(capture, (ex, ey), (ex+ew, ey+eh),(0, 255, 0), 2)


    key = cv2.waitKey(1) & 0xFF
    if key == 27: #Esse 27 é o esc
        break

cv2.destroyAllWindows()
cap.release