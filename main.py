# chromium-browser --start-fullscreen http://raspberrypi.local:5000

from subprocess import Popen
from time import sleep
import os

Popen(["python3", "/home/pi/tempcheck/app.py"])
sleep(5)
Popen(["python3", "/home/pi/tempcheck/camera_stream.py"])
sleep(5)
Popen(["python3", "/home/pi/tempcheck/rec_vdo.py"])
sleep(5)
os.system("chromium-browser --start-fullscreen http://raspberrypi.local:5000")