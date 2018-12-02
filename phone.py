#import libraries
import os
from time import sleep
import time 
import RPi.GPIO as GPIO
from subprocess import call
import random

import pygame 
from pygame.locals import *

#Init GPIO pins
GPIO.setmode(GPIO.BCM)

button1 = False
button2 = False
button3 = False
button4 = False
button5 = False
button6 = False
button7 = False
button8 = False
button9 = False
phonecall = False

#Callback function for phone handle
def my_callback(channel):
    global state
    global phonecall
    #time.sleep(0.01)
    if GPIO.input(channel)==True:  
        phonecall = True
        print('phonecall starts')
        pygame.mixer.music.stop()
        state = INTRO
    else:
        phonecall = False
        
#Callback functions for buttons       
def my_callback1(channel):
    global button1
    time.sleep(0.005)
    if GPIO.input(channel)==False: 
        pygame.mixer.music.stop()
        button1 = True
    #else:
    #    button1 = False
    #    print('false alarm')
        
def my_callback2(channel):
    global button2
    time.sleep(0.005)
    if GPIO.input(channel)==False: 
        pygame.mixer.music.stop()
        button2 = True
    #else:
    #    button2 = False
    #    print('false alarm')
        
def my_callback3(channel):
    global button3
    time.sleep(0.005)
    if GPIO.input(channel)==False: 
        pygame.mixer.music.stop()
        button3 = True
    #else:
    #    button3 = False
     #   print('false alarm')
        
def my_callback4(channel):
    global button4
    time.sleep(0.005)
    if GPIO.input(channel)==False: 
        pygame.mixer.music.stop()
        button4 = True
    #else:
    #    button4 = False
    #    print('false alarm')
        
def my_callback5(channel):
    global button5
    time.sleep(0.005)
    if GPIO.input(channel)==False: 
        pygame.mixer.music.stop()
        button5 = True
    #else:
     #   button5 = False
      #  print('false alarm')
        
def my_callback6(channel):
    global button6
    time.sleep(0.005)
    if GPIO.input(channel)==False: 
        pygame.mixer.music.stop()
        button6 = True
    #else:
     #   button6 = False
     #   print('false alarm')
        
def my_callback7(channel):
    global button7
    time.sleep(0.005)
    if GPIO.input(channel)==False: 
        pygame.mixer.music.stop()
        button7 = True
    #else:
    #    button7 = False
     #   print('false alarm')
def my_callback8(channel):
    global button8
    time.sleep(0.005)
    if GPIO.input(channel)==False: 
        pygame.mixer.music.stop()
        button8 = True
    #else:
    #    button8 = False
     #   print('false alarm')
def my_callback9(channel):
    global button9
    time.sleep(0.005)
    if GPIO.input(channel)==False: 
        pygame.mixer.music.stop()
        button9 = True
    #else:
    #    button8 = False
    #    print('false alarm')

GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(14, GPIO.BOTH, callback = my_callback)

GPIO.add_event_detect(18, GPIO.FALLING, callback=my_callback1)
GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback2)
GPIO.add_event_detect(24, GPIO.FALLING, callback=my_callback3)
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback4)
GPIO.add_event_detect(8, GPIO.FALLING, callback=my_callback5)
GPIO.add_event_detect(25, GPIO.FALLING, callback=my_callback6)
GPIO.add_event_detect(27, GPIO.FALLING, callback=my_callback7)
GPIO.add_event_detect(21, GPIO.FALLING, callback=my_callback8)
GPIO.add_event_detect(26, GPIO.FALLING, callback=my_callback9)

#declare buttoniables and initialize audio

freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 1   # 1 is mono, 2 is stereo
buffer =  1024  # number of samples (experiment to get right sound)
pygame.mixer.init(freq, bitsize, channels, buffer)
pygame.mixer.music.set_volume(0.7)

#Importing soundfiles
ringtone = 'PhoneProject/french-phone.wav'
intromessage = 'PhoneProject/Intro_30min.wav'
messageA = 'PhoneProject/Message_A.wav'
messageA1 = 'PhoneProject/Message_A1.wav'
messageA21 = 'PhoneProject/Message_A2_Congrats.wav'
messageA22 = 'PhoneProject/Message_A2_Sorry.wav'
messageB3D = 'PhoneProject/Message_A3_Dance.wav'
messageB3M = 'PhoneProject/Message_A3_Metal.wav'
messageB3F = 'PhoneProject/Message_A3_Funk.wav'
messageB2 = 'PhoneProject/Message_B2.wav'
messageA3 = 'PhoneProject/Message_B3.wav'

print('start')

def play_sound(music_file):
    '''
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    '''
    global state
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pygame.error:
        print("File {} not found! {}".format(music_file, pygame.get_error()))
        return

    pygame.mixer.music.play()
    
    #try:
    while pygame.mixer.music.get_busy():
        clock.tick(30)
    #finally: 
    #    if(state == MESS_A21 or MESS_A22):
    #        pygame.mixer.music.stop()
    #        state=MESS_A
    
#Declaring the states
PHONERINGS = 0
INTRO = 1
MESS_A = 2
MESS_A1 = 3
MESS_A21 = 4
MESS_A22 = 5
MESS_B3M = 6
MESS_B3D = 7
MESS_B3F = 8
MESS_B2 = 9
MESS_A3 = 10
state = 0



while True:
    b1 = GPIO.input(18)
    b2 = GPIO.input(23)
    b3 = GPIO.input(24)
    b4 = GPIO.input(17)
    b5 = GPIO.input(8)
    b6 = GPIO.input(25)
    b7 = GPIO.input(27)
    b8 = GPIO.input(21)
    b9 = GPIO.input(26)
    
 
    phone = GPIO.input(14) 
    
    print(state)
    if (phonecall == True):
        #print('call')
        if state == INTRO:   
            #play_sound(intromessage)
            state = MESS_A
            print('intro')
            play_sound(intromessage)           
        elif state == MESS_A:
            #Message A : 
            #Press 1 to hear about extra prices
            #Press 2 NOW to try to skip ahead
            #Press 3 to listen to music while watine
            print('message A')
            play_sound(messageA)
           # time.sleep(3)
            if button1==True:
                print('1 prssed')
                state = MESS_A1
                button1 = False
            elif button2==True:
                #Skipping in line
                state = random.randint(4, 5)
                #random choice between two audiofiles
                button2=False
            elif button3==True:
                #Music plays
                print('3  pressed')
                state = MESS_A3
                button3=False

        elif state == MESS_A1:
            #extra prices
            print('message A1')
            play_sound(messageA1)
            time.sleep(2)
            if button9==True:
                #Random choice of message A2
                print('9, A2')
                state = random.randint(4, 5)
                button9=False
            elif button1==True or button2==True or button3==True or button4==True or button5==True or button6==True or button7==True or button8==True:
                #Congratulations message, back to intro
                print('1-8,Going back to A')
                play_sound(messageB2)
                time.sleep(0.2)
                state = MESS_A
                button1=False
                button2=False
                button3=False
                button4=False
                button5=False
                button6=False
                button7=False
                button8=False
                
        elif state == MESS_A21:
            #Try to skip in line
            print('message A21')
            play_sound(messageA21)
            while pygame.mixer.music.get_busy() == True:
                    continue
            state = MESS_A
            
        elif state == MESS_A22:
            print('message A22')
            play_sound(messageA22)
            while pygame.mixer.music.get_busy() == True:
                    continue
            state = MESS_A
            
        elif state == MESS_A3:
            #Listen to music
            print('message A3')
            play_sound(messageA3)
            time.sleep(3)
            if button1==True:
                state = MESS_B3M
                button1=False
            elif button2==True:
                state = MESS_B3D
                button2=False
            elif button3==True:
                state = MESS_B3F
                button3=False
                
        elif state == MESS_B3M: 
            play_sound(messageB3M)
            
            if button5==True:
                print('5, A2')
                state = random.randint(4, 5)
                button5=False
            else:
                while pygame.mixer.music.get_busy() == True:
                    continue
                state = MESS_A
                
        elif state == MESS_B3D: 
            play_sound(messageB3D)
            if button5==True:
                print('5, A2')
                state = random.randint(4, 5)
                button5=False
            else:
                while pygame.mixer.music.get_busy() == True:
                    continue
                state = MESS_A
                
        elif state == MESS_B3F: 
            play_sound(messageB3F)
            if button5==True:
                print('5, A2')
                state = random.randint(4, 5)
                button5=False
            else:
                while pygame.mixer.music.get_busy() == True:
                    continue
                state = MESS_A
                
    #Phone ringing            
    else:
        state = PHONERINGS
        print('no call')
        time.sleep(5)
        play_sound(ringtone)

#if (distance < 50):
    #phone rings
#if (klyka == 1): #person picks up
#        phonecall = true
        
#while phonecall:
    #Intro message plays: Options A are given
    #Nested if-statements begin:
#    if (button 1 is pressed)
#    else if(button 2 is pressed)
#    else if (button 3 is pressed)
    
#    if(klyka == 0): #person hangs up
        #Phonecall is ended, break out of while-loop
#        phonecall = false
        