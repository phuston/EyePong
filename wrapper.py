from subprocess import Popen, PIPE
import serial
from time import sleep

serOut = ser.readline()

control_left_sequence = '''keydown Control_L
key F4
keyup Control_L
'''

shift_right_sequence = '''keydown Shift_L
key A
keyup Shift_L
'''

def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)

keypress(shift_a_sequence)
keypress(control_f4_sequence)