import datetime
import os
from picamera import PiCamera
from time import sleep

minute = 60  # seconds
numberOfImagesPerDay = 150
repeatAfter = minute * 5
rootDirectory = "/home/pi/caps/"

def createFolder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

for i in range(numberOfImagesPerDay):
    todaysDirectory = rootDirectory + datetime.datetime.now().strftime("%y-%m-%d")
    currentTime = datetime.datetime.now().strftime("%H-%M")
    createFolder(todaysDirectory)
    imageName = (todaysDirectory + '/' +currentTime) + ('--%s.jpg' % i)

    #initialize camera
    camera = PiCamera()
    camera.brightness=55

    #Capture image

    #camera.start_preview(alpha=255)
    camera.capture(imageName)
    #camera.stop_preview()
    sleep(repeatAfter)



