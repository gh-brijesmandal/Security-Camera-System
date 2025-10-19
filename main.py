import cv2
import time
import datetime


# creating camera object
cam = cv2.VideoCapture(0)  # given access to default camera

# importing the cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  # detects faces
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")  # detects body

detection = True # face or body detection object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")    #compression method
frame_size = (int(cam.get(3)),int(cam.get(4))) #get heigth and width from the camera object of VideoCapture Class
out = cv2.VideoWriter("video.mp4", fourcc, 20, frame_size)

while True:
    _, frame = cam.read()  # read each frame 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # changes frame to gray color
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # detects face and sends x,y,width,height of faces in list
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5) # detects face and sends x,y,width,height of faces in list
    
    # for (x,y,width,height) in faces:
    #     cv2.rectangle(frame, (x,y), (x+width,y+height), (255,0,0), 3)

    if (len(faces) + len(bodies) > 0):  # if either face or body detected
        detection = True
    
    out.write(frame) # write the frame in video

    cv2.imshow("Camera", frame)  # show the frame read

    if cv2.waitKey(1) == ord('q'):   # code to break from the loop 
        break

out.release()
cam.release()   # released device camera from the object
cv2.destroyAllWindows()   