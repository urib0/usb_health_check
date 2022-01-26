import os
import sys
import serial

BASE_DIR = "/dev/serial/by-id/"
#BASE_DIR = "/home/pi/test"
SERIAL_RATE = 9600

deviceList = os.listdir(BASE_DIR)
series_list = ["co2","temp","hum","lx","uv","moisture"]

if len(deviceList) == 0:
    print("デバイスが見つかりませんでした")
    sys.exit()

for device in deviceList:
    try:
        readSer = serial.Serial(BASE_DIR + device, SERIAL_RATE, timeout=3)
        raw = readSer.readline().decode().replace('\n', '')
        s = []
        for i in range(len(raw.split(";"))):
            s.append(raw.split(";")[i].split("=")[0])
        device_name = ""
        for i in range(len(s)):
            if s[i] in series_list:
                device_name += s[i]
        if len(device_name) == 0:
           print("unknown:" + BASE_DIR + device)
        else:
            print(device_name + ":" + BASE_DIR + device)
    except Exception as e:
        print('failed: ', e)
