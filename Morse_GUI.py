from tkinter import *
import tkinter.font
from gpiozero import LED
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#Variables
interval = 0.4

#Hardware
led=LED(14)

#GUI
win = Tk()
win.title("Morse Code")
textInput = StringVar()

#Letter array
LETTER_CODE = { 
    'A': '.- ', 
    'B': '-... ', 
    'C': '-.-. ', 
    'D': '-.. ', 
    'E': '. ', 
    'F': '..-. ', 
    'G': '--. ', 
    'H': '.... ', 
    'I': '.. ', 
    'J': '.--- ', 
    'K': '-.- ', 
    'L': '.-.. ', 
    'M': '-- ', 
    'N': '-. ', 
    'O': '--- ', 
    'P': '.--. ', 
    'Q': '--.- ', 
    'R': '.-. ' , 
    'S': '... ' , 
    'T': '- ', 
    'U': '..- ', 
    'V': '...- ', 
    'W': '.-- ', 
    'X': '-..- ', 
    'Y': '-.-- ', 
    'Z': '--.. ', }




#Functions
def dot():
    led.on()
    time.sleep(interval)
    led.off()
    time.sleep(interval)

def dash():
    led.on()
    time.sleep(interval*3)
    led.off()
    time.sleep(interval)
    
def letterSpace():
    time.sleep(interval*3)
    

def convertToMorse():
    #while True:
        word = entry.get()
        for letter in word:
                for symbol in LETTER_CODE[letter.upper()]:
                    if symbol == '-':
                        dash()
                    elif symbol == '.':
                        dot()
                    elif symbol == ' ':
                        letterSpace()
                        

def close():
    GPIO.cleanup()
    win.destroy()


#Widgets
Label(win, text = 'Enter Word').grid(row=1,column=0)

entry = Entry(win, )
entry.grid(row=1,column=2)

ledButton = Button(win, text='Enter', command=convertToMorse, height=1, width=12)
ledButton.grid(row=3,column=2)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()