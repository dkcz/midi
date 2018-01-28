import RPi.GPIO as GPIO
import time
import pygame
import sys
from mido import MidiFile 
import mido


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)




music = "moments.mp3"

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(music)



b1 = 27
b2 = 17
b3 = 23
b4 = 18
b5 = 22

def allOff():
	setOff(b1)
	setOff(b2)
	setOff(b3)
	setOff(b4)
	setOff(b5)


def setOn(pin):
	GPIO.output(pin,GPIO.HIGH)

def setOff(pin):
	GPIO.output(pin,GPIO.LOW)

def blink(pin):
	setOn(pin)
	time.sleep(0.25)
	setOff(pin)


def getPin(note):
	if note == 60:
		return 22
	elif note == 62:
		return 18
	elif note == 64:
		return 23
	elif note == 65:
		return 17
	elif note == 67:
		return 27

allOff()

md = MidiFile('moments.mid')

track = md.tracks[1]

print(track)


pygame.mixer.music.play()

time.sleep(0.40)

playing = False

for msg in track:
	if not msg.is_meta:
		time.sleep(mido.tick2second(msg.time,md.ticks_per_beat, 526316))
		if msg.type == "note_on":
			setOn(getPin(msg.note))
		elif msg.type == "note_off":
			setOff(getPin(msg.note))




