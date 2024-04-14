import RPi.GPIO as GPIO
from tkinter import *
root=Tk()
root.geometry('300x300')
GPIO.setmode(GPIO, BCM)
red_LED=GPIO.setup(18, GPIO.OUT)


def red():
   LED=GPIO.input(red_LED)
   if LED==HIGH:
    GPIO.output(red_LED, GPIO.LOW)
    red_button['text']='RED OFF'
   else:
        GPIO.output(red_LED, GPIO.HIGH)

red_button=Button(root, text='Red OFF', bg='red').pack()



root.mainloop()
