#Ejemplo de deteccion facial con OpenCV y Python
#Por Glare
#www.robologs.net
 
import numpy as np
import cv2
 
#cargamos la plantilla e inicializamos la webcam:
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascades/haarcascade_frontalface_alt_tree.xml')
cap = cv2.VideoCapture(1)

w = cap.get(3) #get width
h = cap.get(4) #get height

mx = int(w/2)
my = int(h/2)

count = 0
 
while(True):
    #leemos un frame y lo guardamos
	ret, img = cap.read()
    
    #try:
	count = count + 1
	text = "Hello World " + str(count)
	cv2.putText(img, text ,(mx,my),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv2.LINE_AA)
	#cv2.imshow('Frame',frame)
	#img = cv2.resize(img, (240,180)) 
	#convertimos la imagen a blanco y negro
	#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    #buscamos las coordenadas de los rostros (si los hay) y
    #guardamos su posicion
	#faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
    #Dibujamos un rectangulo en las coordenadas de cada rostro
	#for (x,y,w,h) in faces:
	#	cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
 
    #Mostramos la imagen
	cv2.imshow('img',img)
     
    #con la tecla 'q' salimos del programa
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
