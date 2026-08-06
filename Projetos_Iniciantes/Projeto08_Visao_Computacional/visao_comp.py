#%%
import cv2
from cvzone.HandTrackingModule import HandDetector

#%%
webcam = cv2.VideoCapture(0)
rastreador_maos = HandDetector(detectionCon=0.8, maxHands=2)    # 80% de certeze que é uma mão e 2 mãos no total.

# Altera o tamanho da janela da câmera:
cv2.namedWindow("Visão Computacional com Python", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Visão Computacional com Python", 540, 400)

# Modificando a resolução: 
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 660)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
 
while True:
    sucesso, imagem = webcam.read()
    coordenadas, imagem_maos = rastreador_maos.findHands(imagem)
    cv2.imshow("Visão Computacional com Python", imagem)

    # print(coordenadas)

    if cv2.waitKey(1) != -1:
        break

# libera a câmera
webcam.release()

cv2.destroyAllWindows()

  
# %%
