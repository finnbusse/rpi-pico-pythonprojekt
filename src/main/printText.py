from machine import Pin
import LCD1602

lcd = LCD1602.LCD1602(16,2)

def printText(line1, line2):
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.printout(line1[:16])
    lcd.setCursor(0, 1)
    lcd.printout(line2[:16])
