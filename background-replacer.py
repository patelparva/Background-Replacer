from turtle import back
import cv2
import time
import numpy as np

fourcc=cv2.VideoWriter_fourcc(*'XVID')
output_file=cv2.VideoWriter('output.avi',fourcc,20,(640,480))

cap=cv2.VideoCapture(0)

background=cv2.imread('background-image.jpg',cv2.IMREAD_COLOR)
background=np.flip(background,axis=1)
background=cv2.resize(background,(640,480))

time.sleep(2)

while (cap.isOpened()):
    ret,img=cap.read()

    img=np.flip(img,axis=1)

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower_red=np.array([0,0,0])
    upper_red=np.array([179, 255, 85])

    mask_1=cv2.inRange(hsv,lower_red,upper_red)

    mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))

    mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

    mask_2=cv2.bitwise_not(mask_1)

    res_1=cv2.bitwise_and(img,img,mask=mask_1)

    res_2=cv2.bitwise_and(background,background,mask=mask_2)

    final_output=cv2.addWeighted(res_1,1,res_2,1,0)

    output_file.write(final_output)

    cv2.imshow('Magic',final_output)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
output_file.release()
cv2.destroyAllWindows()

# cv2.imshow('image', background)
# cv2.waitKey(0)
# cv2.destroyAllWindows()