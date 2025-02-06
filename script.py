import cv2
import numpy as np

imagem = cv2.imread('/app/imagens/objeto.jpg')

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

imagem_suavizada = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)

_, imagem_binaria = cv2.threshold(imagem_suavizada, 100, 255, cv2.THRESH_BINARY_INV)

contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

num_objetos = len(contornos)

cv2.drawContours(imagem, contornos, -1, (0, 255, 0), 2)

# Adicionar texto com o número de objetos
cv2.putText(imagem, f"Objetos: {num_objetos}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Salvar o resultado em um arquivo
cv2.imwrite('/app/imagens/resultado.jpg', imagem)

