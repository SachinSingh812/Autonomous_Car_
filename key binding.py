#this will assign the frames left,right,up,down values while training the car.

import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")
id=input("Enter user id")
img_counter = 0

while True:
    ret, frame = cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 2490368:
        # UPKEY pressed
        #img_name = "opencv_frame_{}.png".format(img_counter)
        img_counter += 1
        cv2.imwrite("dataSet1/User."+str(id)+"."+str(sampleNum)+".jpg",gray)
        #cv2.imwrite(img_name, frame)
        #print("{} written!".format(img_name))
        #img_counter += 1
    elif k%256 == 2621440:
        # DOWNKEY pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite("dataSet1/User.",frame)
        #cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
    elif k%256 == 2424832:
        # LEFTKEY pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite("dataSet1/User.",frame)
        #cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
    elif k%256 == 255904:
        # RIGHTKEY pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite("dataSet1/User.",frame)
        #cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
