import cv2
import numpy as np
cam=cv2.VideoCapture(0)
kernel=np.ones((5,5),np.uint8)
while(True):
	red,frame=cam.read()

	rangomax=np.array([119,255,51])# Color mas claro
	rangomin=np.array([0,51,0])# Color mas oscuro
	mascara=cv2.inRange(frame,rangomin,rangomax)
	opening=cv2.morphologyEx(mascara,cv2.MORPH_OPEN,kernel)
	x,y,w,h=cv2.boundingRect(opening)
	img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
	cv2.circle(frame,(int(x+w/2),int(y+h/2)),5,(0,0,255),-1)
	cv2.putText(img,"Green",(x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
	cv2.imshow('camara',frame)
	k=cv2.waitKey(1) & 0xFF
	if k==27:
		break
