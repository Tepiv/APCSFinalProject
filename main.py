import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([50, 30, 50])
    upper_blue = np.array([130, 250, 255])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    #cv2.imshow('frame', result)
    #cv2.imshow('mask', mask)

    (h, w) = frame.shape[:2]
    
    centerX, centerY = (w // 2), (h // 2)

    
    topHalf = mask[centerY:h, 0:w]
    bottomHalf = mask[0:centerY, 0:w]
    leftHalf = mask[0:h, 0:centerX]
    rightHalf = mask[0:h, centerX:w]
    middleRadius = 50
    middle = mask[centerY-middleRadius:centerY+middleRadius,centerX-middleRadius:centerX+middleRadius]

    success = (middleRadius*2)**2*255*0.3    

    

    a = np.sum(leftHalf)
    b = np.sum(rightHalf)
    c = np.sum(topHalf)
    d = np.sum(bottomHalf)
    e = np.sum(middle)
    

    #move left/move right

    if e > success:
        #stop
        print("gaming time")
    #if  a > b:
        #move left
        #print("left")
    #elif b > a:
        #move right
        #print("right")

    #cv2.imshow('Left Half', leftHalf)
    #cv2.imshow('Right Half', rightHalf)  
    #cv2.imshow('Top Half', topHalf)
    #cv2.imshow('Bottom Half', bottomHalf)      
    cv2.imshow('Middle', middle)

    if cv2.waitKey(1) == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()



