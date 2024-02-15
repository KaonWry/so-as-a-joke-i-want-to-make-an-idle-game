import os
import time
import keyboard

def mainLoop():
    os.system('cls');
    print (addValue());
    time.sleep(0.1);
    
def addValue():
    global value;
    value += 0.1 * multiplier();
    return round(value, 2);

def multiplier():
    # global mult;
    mult = 5;
    return mult;

value = 0;

while True:
    mainLoop()
    try:
        if keyboard.is_pressed('esc'):
            exit();
    except:
        break;
    