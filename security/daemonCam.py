import datetime
import os
from picamera import PiCamera
from time import sleep

camera = PiCamera()

# camera.start_preview(alpha=250)
# camera.rotation=180

minute = 60  # seconds
numberOfImagesPerDay = 150

rootDirectory = "/home/pi/caps/"

def createFolder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

for i in range(numberOfImagesPerDay):
    todaysDirectory = rootDirectory + datetime.datetime.now().strftime("%y-%m-%d")
    currentTime = datetime.datetime.now().strftime("%H-%M")
    createFolder(todaysDirectory)
    imageName = todaysDirectory + currentTime + ('--%s.jpg' % i)
    camera.capture(imageName)
    sleep(minute * 5)

# camera.stop_preview()