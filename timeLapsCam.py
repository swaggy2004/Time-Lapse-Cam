'''
This program is made to take continous pictures inorder to make a timelaps video

~ Shaveen Balasooriya
'''
from picamera import PiCamera
from time import sleep, strftime, localtime, time
import sys

camera = PiCamera()

camera.resolution = (2592, 1944)
camera.framerate = 20

def getTime():
    current_time = time()
    formatted_time = strftime('%Y-%m-%d_%H:%M:%S', localtime(current_time)) 
    print(formatted_time)
    return formatted_time
    
try:
    camera.start_preview()
    while True:
        print('Getting time...')
        time_stamp = str(getTime())
        print('Taking image...')
        camera.capture(f'/home/shaveen/Pictures/Timelaps/{time_stamp}.jpg')
        sleep(30)
except Exception as e:
    camera.stop_preview()
    print(f'Exit due to erro: {e}')
    sys.exit(0)
except KeyboardInterrupt:
    camera.stop_preview()
    print('Clean exsit...')
    sys.exit(0)