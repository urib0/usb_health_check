import os
import sys
import serial

BASE_DIR = "/dev/serial/by-id/"
#BASE_DIR = "/home/pi/test"

deviceList = os.listdir(BASE_DIR)

if len(deviceList) == 0:
    print("デバイスが見つかりませんでした")
    sys.exit()

