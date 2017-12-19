#!/bin/sh

#sudo apt-get install gnome-schedule   #uncomment this if crontab is not installed

crontab -e 0 8 * * *  /home/pi/backup.sh  #run this everyday @ 8 am

# m h  dom mon dow   command
# * * * * *  command to execute
# ┬ ┬ ┬ ┬ ┬
# │ │ │ │ │
# │ │ │ │ │
# │ │ │ │ └───── day of week (0 - 7) (0 to 6 are Sunday to Saturday, or use names; 7 is Sunday, the same as 0)
# │ │ │ └────────── month (1 - 12)
# │ │ └─────────────── day of month (1 - 31)
# │ └──────────────────── hour (0 - 23)
# └───────────────────────── min (0 - 59)


#RUN A TASK ON REBOOT
#To run a command every time the Raspberr y Pi starts up, write @reboot instead of the time and date. For example:

@reboot python /home/pi/tab/security/daemonCam.py  &

# & indicates background task