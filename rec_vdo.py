import numpy as np 
import cv2
import time
import sched, time

timerecord = 900 # 15 min
t = time.localtime()
current_time = time.strftime("%Y%m%d_%H%M%S", t)
# print(current_time)



# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

while(True):
    try :
        t = time.localtime()
        current_time = time.strftime("%Y%m%d_%H%M%S", t)
        cap = cv2.VideoCapture() 
        cap.open("http://raspberrypi.local:8000/stream.mjpg")
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        out = cv2.VideoWriter('{}.avi'.format(current_time), fourcc, 20, (320,240))
        starttime = time.time()
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # cv2.putText(frame, '36.7 Celsius', (10,450), font, 2, (0, 255, 0), 2, cv2.LINE_AA)

            # cv2.imshow('camera',frame)
            out.write(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            elif time.time() - starttime >= timerecord:
                break

            else:
                print(time.time() - starttime)

        # When everything done, release the capture 
        cap.release()
        out.release()
        # cv2.destroyAllWindows()

    except Exception as e:
        print(e)
        pass