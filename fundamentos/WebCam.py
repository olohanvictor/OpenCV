import cv2

cap = cv2.VideoCapture(0)
larg = 640
altu = 360

while True: #Pra ser verificado todo frame do vídeo
    ret,video = cap.read()

    capture = cv2.resize(video, (larg,altu), fx = 0, fy = 0, interpolation= cv2.INTER_AREA) #Img da webcam
    gray = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY) #Img cinza, menos informações pro pc processar
    cv2.imshow('video', capture)
    cv2.imshow('cinza', gray)

    key = cv2.waitKey(30) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()