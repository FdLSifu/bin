#!/usr/bin/python3
import subprocess
import json
import time
import signal 
DIR="/home/fdlsifu/Pictures/"
WALLMOR1="macos-catalina-mountains-island-daytime-stock-5k-6016x6016-188.jpg"
WALLMOR2="macos-catalina-mountains-island-morning-stock-5k-6016x6016-4015.jpg"
WALLMOR3="macos-catalina-mountains-island-morning-foggy-stock-5k-6016x6016-4019.jpg"
WALLDAY="macos-catalina-mountains-island-sunny-day-stock-5k-6016x6016-4013.jpg"
WALLEVE1="macos-catalina-mountains-island-evening-stock-5k-6016x6016-4021.jpg"
WALLEVE2="macos-catalina-mountains-island-evening-twilight-sunset-6016x6016-4009.jpg"
WALLEVE3="macos-catalina-mountains-island-night-cold-stock-5k-6016x6016-4022.jpg"
WALLNIGHT="macos-catalina-mountains-island-night-stock-5k-6016x6016-189.jpg"

def set_wp(a,b):
    current_h = time.gmtime().tm_hour

    if current_h < 6 or current_h > 19:
        wall = DIR+WALLNIGHT
    elif current_h == 6:
        wall = DIR+WALLMOR1
    elif current_h == 7:
        wall = DIR+WALLMOR2
    elif current_h == 8:
        wall = DIR+WALLMOR3
    elif current_h > 8 and current_h < 17:
        wall = DIR+WALLDAY
    elif current_h == 17:
        wall = DIR+WALLEVE1
    elif current_h == 18:
        wall = DIR+WALLEVE2
    elif current_h == 19:
        wall = DIR+WALLEVE3
    else:
        wall = DIR+WALLNIGHT
    subprocess.run(['/home/fdlsifu/.fehbg'])
    xrandr = subprocess.Popen(['xrandr'],stdout=subprocess.PIPE)
    res = subprocess.check_output(['awk', "/*/ {print $1;exit;}"],stdin=xrandr.stdout)
    xrandr.wait()
    res = res.decode()
    subprocess.run(['convert','-gravity','center','-geometry',res+"^",'-crop',res+'+0+0',wall,'/tmp/current_wall.png'])
    # gnome
    #run(['gsettings', 'set' ,'org.gnome.desktop.background', 'picture-uri', "'file://"+wall+"'"])
    # else
    subprocess.run(['feh', '--bg-fill' ,wall])

signal.signal(signal.SIGUSR1,set_wp)

while(True):
    try:
       set_wp(0,0)
       time.sleep(5*60) # sleep 5 minutes
    except Exception as e:
        print("Exception",e)
        continue
