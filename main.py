import numpy as np
import cv2
import serial
import time

cap = cv2.VideoCapture(0)
ser = serial.Serial('COM3', 9600)
shooting = False

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([50, 30, 50])
    upper_blue = np.array([130, 250, 255])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)



    cv2.imshow('mask', mask)

    key = cv2.waitKey(1)
    
    if  key == ord('q'):
        break
    elif key == ord(' '):
        shooting = True

    if (not shooting):
        continue
    (h, w) = frame.shape[:2]
    
    centerX, centerY = (w // 2), (h // 2)

    width = 50
    height = 150

    leftHalf = mask[0:h, 0:centerX]
    rightHalf = mask[0:h, centerX:w]
    middle = mask[centerY-height:centerY+height,centerX-width:centerX+width]

    success = (width*height*4)*255*0.1    

    

    a = np.sum(leftHalf)
    b = np.sum(rightHalf)
    e = np.sum(middle)
    

    #move left/move right

    if e > success:
        #stop
        shooting = False
        ser.write('S'.encode())
        time.sleep(2)
    elif  a > b:
        #move left
        ser.write('L'.encode())
        time.sleep(0.5)
       
    elif b > a:
        #move right
        ser.write('R'.encode())
        time.sleep(0.5)
        


        


    #cv2.imshow('Left Half', leftHalf)
    #cv2.imshow('Right Half', rightHalf)  
  
    cv2.imshow('Middle', middle)

    

cap.release()
cv2.destroyAllWindows()
ser.write(b'Q') 


