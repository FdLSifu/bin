#!/usr/bin/python3

import sys
from tl100 import TL100Lamp

cmds = ['night','on','off']

def usage():
    print("Usage: tl100 [night|on brightness_level(1-100)]")
    exit()

if len(sys.argv) == 1:
    usage()
elif len(sys.argv) == 2 and not sys.argv[1] in cmds:
    usage()



lamp = TL100Lamp(device_id="57:4C:42:DF:93:66")

if sys.argv[1] == "night":
    lamp.stop_solar_mode()
    lamp.start_color_mode()
    lamp.set_color("FF6000")
    v = 100
    lamp.set_color_brightness(v)

elif sys.argv[1] == "on":
    lamp.stop_color_mode()
    lamp.start_solar_mode()

elif sys.argv[1] == "off":
    lamp.stop_color_mode()
    lamp.stop_solar_mode()

lamp.disconnect()

