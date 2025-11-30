#Cores trazem muita informação pra uma imagem. aos remove-lás, a imagem fica mais simples.

import cv2  # importa OpenCV

imgcolorida = cv2.imread("src/pic.jpg", cv2.IMREAD_COLOR)# carrega "pic.jpg". IMREAD_GRAYSCALE é autoexplicativo
imgcinzenta= cv2.imread("src/pic.jpg", cv2.IMREAD_GRAYSCALE)# carrega "pic.jpg". IMREAD_GRAYSCALE é autoexplicativo

#Criando valores para redimencionar as imagens
escala = 25 #Tamanho q eu quero em %tagem
largura = int((imgcolorida.shape[1]*escala)/100) #1 é altura
altura = int((imgcolorida.shape[0]*escala)/100) #shape[0] é largura 

dim = (largura,altura) #variavel q guarda largura e a altura, já q o cv2.resize só aceita uma variavel pro tamanho

imgcor = cv2.resize(imgcolorida, dim, interpolation= cv2.INTER_AREA) #Redimensionando a imagem colorida
imgcinza = cv2.resize(imgcinzenta, dim, interpolation= cv2.INTER_AREA)#Redimensionando a imagem cinza


cv2.imshow("Imagem com cor", imgcor)
cv2.imshow("Imagem sem cor", imgcinza)

cv2.waitKey(0) #0 = espera infinita (ms)
cv2.destroyAllWindows () #Fecha todas as janelas do OpenCV

