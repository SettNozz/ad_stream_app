import cv2
import sockTest
import os

cam2 = 'rtmp://localhost/myapp/mystream'
cap = cv2.VideoCapture()
cap.open(cam2)
overlay = None
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('outstream.avi',fourcc, 20.0, (1092, 614))
counter = 0
countStop = 0
time = 0
a = 0

while(cap.isOpened()):
    #os.system("gnome-terminal -e 'bash -c \"ffmpeg -re -i /home/settnozz/python_stream/outstream.avi -c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 -f flv rtmp://live.twitch.tv/settnozz/live_64609648_vOa0jBYpxpYNbE0HoXjlf8ENxNDwLK; exec bash\"'")
    ret, frame = cap.read()
    if frame is None:
        continue


    maybeImage, time, x, y  = sockTest.maybeNewImage()
    if maybeImage is not None and time is not None and x is not None and y is not None:
        overlay = maybeImage
        IKS = x
        IGR = y
        print (time)
        countStop = time


    if overlay != None and countStop != None and IKS != None and IGR != None:
        counter +=1
        h2, w2 = overlay.shape[:2]
        frame[IKS:h2 + IKS , IGR:w2 + IGR, :] = overlay
        if counter == countStop:
            overlay, countStop, counter, IKS, IGR = None, 0, 0, 0, 0
    #out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
