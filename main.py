import os
import sys
import serial

BASE_DIR = "/dev/serial/by-id/"
#BASE_DIR = "/home/pi/test"
SERIAL_RATE = 9600

deviceList = os.listdir(BASE_DIR)

if len(deviceList) == 0:
    print("デバイスが見つかりませんでした")
    sys.exit()

for device in deviceList:
    try:
        readSer = serial.Serial(BASE_DIR + device, SERIAL_RATE, timeout=3)
        raw = readSer.readline().decode().replace('\n', '')
        s = ""
        for i in range(len(raw.split(";")) - 2):
            s += raw.split(";")[i].split("=")[0]
        if len(s) == 0:
            print("unknown:" + BASE_DIR + device)
        else:
            print(s + ":" + BASE_DIR + device)
    except requests.exceptions.RequestException as e:
        print('request failed: ', e)