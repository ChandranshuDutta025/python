import pyautogui as pag
import random as rand
import time

while True:  # Infinite loop
    x = rand.randint(100, 700)  # Correct randint function
    y = rand.randint(200, 700)
    pag.moveTo(x, y)
    time.sleep(5)
