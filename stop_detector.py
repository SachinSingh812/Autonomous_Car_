import cv2
import numpy as np

stop=cv2.CascadeClassifier('stop.xml')
traffic=cv2.CascadeClassifier('traffic.xml')
cam=cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read(r"C:\Users\hp\Desktop\Projects\face Detector\recognizer\trainingData.yml")
id=0

fontface = cv2.FONT_HERSHEY_COMPLEX
fontscale=0.8
fontcolor=(0,255,0)
while True:
    check,img=cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop_sign=stop.detectMultiScale(gray,1.3,5)
    traffic_sign=traffic.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in stop_sign :
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(id==1):
            id="stop"
        cv2.putText(img,str(id),(x,y-10),fontface,fontscale,fontcolor)
        
    for(x,y,w,h) in traffic_sign :
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        #if(id==2):
            #id="red"
        #elif(id==3):
            #id="green"
        #elif(id==4):
            #id="yellow"
        cv2.putText(img,str(id),(x,y-10),fontface,fontscale,fontcolor)

    cv2.imshow("Camera",img)
    if (cv2.waitKey(1)== ord('q')):
        break
cam.release()
cv2.destroyAllWindows()

