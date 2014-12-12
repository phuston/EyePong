from subprocess import Popen, PIPE
import serial
from time import sleep

ser = serial.Serial(port='COM11', baudrate=9600) #Create connection with Arduino

serOut = ser.readline()

control_left_sequence = '''key A
key S
key S
'''

control_right_sequence = '''key T 
key I 
key T
key S
'''

def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)

while True:
	serOut = ser.readline()
	if(serOut == "Left"):
		keypress(control_left_sequence)
	elif(serOut == "Right"):
		keypress(control_right_sequence)
