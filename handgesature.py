import cv2
import mediapipe as mp 
import time  
cap =cv2.VideoCapture(1)

mpHands=mp.solutions.hands 
hands=mpHands.Hands()





while True: 
    success, img =cap.read()
    
    
    imgRGB= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    print(results)
    print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            
    
    cv2.imshow("image",img)
    cv2.waitKey(1)
