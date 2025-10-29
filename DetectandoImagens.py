import cv2  # importa OpenCV

img = cv2.imread("pic.jpg", cv2.IMREAD_COLOR)  #Carrega "pic.jpg". IMREAD_COLOR faz carregar com as cores
cv2.imshow("Imagem", img) #Mostra a imagem na tela
cv2.waitKey(0) #0 = espera infinita (ms)
cv2.destroyAllWindows# Fecha todas as janelas do OpenCV
