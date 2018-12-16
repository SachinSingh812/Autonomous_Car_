import cv2
stop=cv2.CascadeClassifier('stop.xml')
traffic=cv2.CascadeClassifier('traffic.xml')
cam=cv2.VideoCapture(0)
id=input("Enter user id")
sampleNum=0
while True:
    check,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    stop_sign=stop.detectMultiScale(gray,1.3,5)
    traffic_sign=traffic.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in stop_sign:

        sampleNum=sampleNum+1
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100)

    for (x, y, w, h) in traffic_sign:
        sampleNum = sampleNum + 1
        cv2.imwrite("dataSet/User." + str(id) + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.waitKey(100)

    cv2.imshow("Camera",img)
    cv2.waitKey(1)
    if(sampleNum>50):
        break
cam.release()
cv2.destroyAllWindows()