import LCD1602
from time import sleep
import time
import apps
from machine import Pin

buttonBack = Pin(15, Pin.IN, Pin.PULL_DOWN)
buttonOk = Pin(14, Pin.IN, Pin.PULL_DOWN)
buttonNext = Pin(13, Pin.IN, Pin.PULL_DOWN)        #vollständig und funktionsfähig
lcd=LCD1602.LCD1602(16,2)
sleep = time.sleep

appId = 0


def boot():
    lcd.clear()
    loading = ""
    lcd.setCursor(0, 0)
    lcd.printout("Pico is booting"[:16])
    for _ in range(16):
        loading += "-"
        lcd.setCursor(0, 1)
        lcd.printout(loading[:16])
        
        sleep(0.15)
        
    getNum()



def printText(line1, line2):
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.printout(line1[:16])
    lcd.setCursor(0, 1)
    lcd.printout(line2[:16])
    
def checkNum(appId):
    if 1 <= appId <= 5:
        printText("App wird ausge-", "fuehrt: "+str(appId))
        sleep(1)
        apps.startApp(appId)
    
    else:
        printText("Diese App ist", "nicht verfuegbar!")
        sleep(2)
        appId = 0
        getNum()
        
        
        
        
    
def getNum():
    global appId
    printText("Bitte waehle", "eine App aus")
    while True:
        while buttonNext.value():
            appId += 1
            printText("App:", str(appId))
            sleep(0.05)
            while buttonNext.value():
                sleep(0.01)
                pass
        
        while buttonBack.value():
            appId -= 1
            printText("App:", str(appId))
            sleep(0.05)
            while buttonBack.value():
                sleep(0.01)
                pass
        
        while buttonOk.value():
            checkNum(appId)
            
        while 6 <= appId or (appId <= -1):
            appId = 0
            
            
            
boot()
