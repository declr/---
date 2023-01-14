from Arduino import Arduino
import time

def blink1():
  board.digitalWrite(13, "LOW")
  time.sleep(1)
  board.digitalWrite(13, "HIGH")
  time.sleep(1)

board = Arduino('9600')
board.pinMode(13, "OUTPUT")

while Ture:
    blink1()
