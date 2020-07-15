import numpy as np
from datetime import datetime
import cv2

cap = cv2.VideoCapture('hi.mp4') # Name of video to be used 

video_capturing = False
while(True):
    _, frame = cap.read()
    nameofImg = "cctv" + str(datetime.now().strftime('%d%m%y%H%M%S%f')) + '.jpg'  # name of video includes date and time
    cv2.imshow('original', frame)
    k = cv2.waitKey(1) & 0xff
    if k == 32:   
        print("Image saving.")
        cv2.imwrite(nameofImg, frame)
        print("Image saved.")
    
    if k == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()