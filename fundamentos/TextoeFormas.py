import cv2               # importa OpenCV
import numpy as np       # importa NumPy

imagem = np.zeros((400, 400, 3), dtype='uint8') #Cria imagem preta 400x400 RGB

cv2.line(imagem, (0,170), (400,170), (0,0,255), 5) #Desenha linha vermelha
cv2.rectangle(imagem, (30,30), (200,200), (0,255,0), 3) #Desenha retângulo verde
cv2.circle(imagem, (200,200), 100, (255,0,0), 3) #Desenha círculo azul

font = cv2.FONT_HERSHEY_SIMPLEX #Define fonte do texto
cv2.putText(imagem, 'Chaves Metaleiro', (50,50), font, 0.8, (255,255,255), 2) #Escreve texto branco

cv2.imshow('Imagem', imagem) #Mostra a imagem na tela
cv2.waitKey(0) #Espera tecla ser pressionada
cv2.destroyAllWindows() #Fecha a janela
