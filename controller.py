# Python code for controller native service - controller.py

import time
import datetime
import sqlite3
import RPi.GPIO as GPIO
from omxplayer import OMXPlayer
import requests


# Initialize SQLite
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

# GPIO Setup
GPIO.setmode(GPIO.BCM)
LIGHT_PIN = 25

#define omxplayer
file_path_or_url = '/home/pi/Downloads/music.mp3'
player = OMXPlayer(file_path_or_url)

# # Function to read LDR connected to MCP3008
# def readLDR():
    # light_level = ReadChannel(LIGHT_CHANNEL)
    # lux = ConvertLux(light_level, 2)
    # return lux

# # Function to convert LDR reading to Lux
# def ConvertLux(data, places):
    # R = 10 #10k-ohm resistor connected to LDR
    # volts = (data * 3.3) / 1023
    # volts = round(volts, places)
    # lux = 500 * (3.3 - volts) / (R * volts)
    # return lux

# # Function to read SPI data from MCP3008 chip
# def ReadChannel(channel):
    # adc = spi.xfer2([1, (8 + channel) << 4, 0])
    # data = ((adc[1]&3) << 8) + adc[2]
    # return data

# Get current lightstate from DB
def getCurrentMlight():
    cur.execute('SELECT * FROM MLight_State')
    data = cur.fetchone()  # (1, u'on')
    return data[1]

# Get current musicstate from DB
def getCurrentMusic():
    cur.execute('SELECT * FROM Music_State')
    data = cur.fetchone()  # (1, u'play')
    return data[1]

# Store current lightstate in DB
def setCurrentMlight(val):
    query = 'UPDATE Mlight_State set light = "'+val+'"'
    cur.execute(query)

# Store current music state in DB
def setCurrentMusic(val):
    query = 'UPDATE Music_State set music = "'+val+'"'
    cur.execute(query)

def switchOnLight(PIN):
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)

def switchOffLight(PIN):
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, False)

def runManualMode():
    # Get current state from DB
    currentlightState = getCurrentMlight()
    currentmusicState = getCurrentMusic()
    if currentlightState == 'on':
        print 'Manual - On'
        switchOnLight(LIGHT_PIN)
    elif currentlightState == 'off':
        print 'Manual - Off'
        switchOffLight(LIGHT_PIN)
    if currentmusicState == 'play':
        print 'music - play'
        player.play()
        player.play()
    elif currentmusicState == 'stop':
        print 'music - stop'
        player.quit()
	
		
# am not sure weather we want to store the data in the DB
def setMlightState(val):
    values = {'light': val}
    r = requests.put('http://127.0.0.1:8000/Moring/light/1/', data=values, auth=('syin', 'GODhm0608'))
    
def setMusicState(val):
    values = {'music': val}
    r = requests.put('http://127.0.0.1:8000/Morning/music/1/', data=values, auth=('syin', 'GODhm0608'))
# Controller main function
# def runController():
#     currentMode = getCurrentMode()
#     if currentMode == 'auto':
#         runAutoMode()
#     elif currentMode == 'manual':
#         runManualMode()
#
#     return True

while True:
    try:
        runManualMode()
        time.sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
