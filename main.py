import cv2
import time
import datetime

# creating camera object
cam = cv2.VideoCapture(0)  # given access to default camera

while True:
    _, frame = cam.read()  # read each frame 

    cv2.imshow("Camera", frame)  # show the frame read

    if cv2.waitKey(1) == ord('q'):   # code to break from the loop 
        break

cam.release()   # released device camera from the object
cv2.destroyAllWindows()   