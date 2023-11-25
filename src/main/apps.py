import LCD1602
from time import sleep
import time
from machine import Pin
import random
import math


buttonBack = Pin(15, Pin.IN, Pin.PULL_DOWN)
buttonOk = Pin(14, Pin.IN, Pin.PULL_DOWN)
buttonNext = Pin(13, Pin.IN, Pin.PULL_DOWN)    #Taschenrechner funktioniert noch nicht, behebe ich aber noch (Version von 18.10.2023)
lcd=LCD1602.LCD1602(16,2)
sleep = time.sleep


def printText(line1, line2):
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.printout(line1[:16])
    lcd.setCursor(0, 1)
    lcd.printout(line2[:16])
    

def startApp(id):
    if id == 1:
        clock()
        
    elif id == 2:
        cube()
        
    elif id == 3:
        calculator()
        
    elif id == 4:
        printText("","")
        
    elif id == 5:
        printText("","")
        

#---------Uhr-----------
        
def clock():
    lcd.clear()
    while True:
        lcd.setCursor(0, 0)
        T=list(time.localtime())
        T[6]+=1
        T=["{:0>2}".format(str(i)) for i in T]
        lcd.printout(T[2]+'.'+T[1]+'.'+T[0])
        lcd.setCursor(0, 1)
        lcd.printout(T[3]+":"+T[4]+":"+T[5])
        sleep(0.1)
        while buttonBack.value():
            return()
        
        
#----------------------
        
#--------Würfel--------

def cube():
    lcd.clear
    printText("Druecke OK,", "um zu wuerfeln.")
    while True:
        while buttonOk.value():
            shakeCube()
            while buttonOk.value():
                sleep(0.1)
                pass
            
        while buttonBack.value():
            return()
            
        
        
        
        
def shakeCube():
    number = random.randrange(1,7)
    printText("Die Zahl ist:", str(number))
    sleep(1)
    printText("Nochmal?", str(number))
        
#-----------------------------
    
#-------Taschenrechner--------
    
number1 = 0
number2 = 0
    
    
def calculator():
    printText("Bitte Rechenart", "auswaehlen:")
    sleep(1)
    printText("Zuruck |  +|  -|", "       v   v   v")
    while True:
        while buttonBack.value():
            return()
    
        while buttonOk.value():
            symbol = "+"
            sleep(0.1)
            getNumber1(symbol)
        
        while buttonNext.value():
            symbol = "-"
            sleep(0.1)
            getNumber1(symbol)
        

def getNumber1(type):
    global number1
    printText("?    " + type + "    ?", "1. Zahl:  " + str(number1))
    while True:
        while buttonBack.value():
            number1 -= 1
            printText("?    " + type + "    ?", "1. Zahl:  " + str(number1))
            sleep(0.05)
            
            while buttonBack.value():
                sleep(0.01)
                pass
            
        
            
        while buttonOk.value():
                
            sleep(0.01)
            
            while buttonOk.value():
                getNumber2(type, number1)
                sleep(0.05)
                pass
            
            
        while buttonNext.value():
            number1 += 1
            printText("?    " + type + "    ?", "1. Zahl:  " + str(number1))
            sleep(0.05)
                
            while buttonNext.value():
                sleep(0.01)
                pass
    
    
    
    
def getNumber2(type, number1):
    global number2
    sleep(0.5)
            
    while True:
        while buttonBack.value():
            number2 -= 1
            printText(str(number1) + type + "    ?", "2. Zahl:  " + str(number2))
            sleep(0.05)
            
            while buttonBack.value():
                 sleep(0.01)
                 pass
            
            
            
        while buttonNext.value():
            number2 += 1
            printText(str(number1) + type + "    ?", "2. Zahl:  " + str(number2))
            sleep(0.05)
            
            while buttonNext.value():
                sleep(0.01)
                pass
            
        
        while buttonOk.value():
            calculate(number1, type, number2)
    
    
def calculate(number1, type, number2):
    total = int(str(number1)) + " " + type + " " + int(str(number2))
    printText("Ergebnis: ", total)
    #printText(str(number1) + type + str(number2), "=     ...")
    
#-----------------------------
