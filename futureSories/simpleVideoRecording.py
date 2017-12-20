from picamera import PiCamera
from time import sleep

camera= PiCamera()
camera.start_preview()
camera.rotation=180
camera.start_recording('/home/pi/Desktop/Kamil.h264')
sleep(10)
camera.stop_recording()
camera.start_preview()
