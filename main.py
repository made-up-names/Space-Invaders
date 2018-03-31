import os
from pynput import keyboard
from spaceship import *
from board import *
from missiles import *
from aliens import *


def on_press(key):
        try:
            k = key.char
        except:
            k = key.name
        if (k == 'a'):
                ship.moveleft()
        elif (k == 'd'):
                ship.moveright()
        elif (k == 'space'):
                mis1(ship.r, ship.c)
        elif (k == 's'):
                mis2(ship.r, ship.c)
        elif (k == 'q'):
                os._exit(0)


# Main code
ship = spaceship(8, 1)
board1.counter()
aliens.spawn()

with keyboard.Listener(on_press=on_press) as lis:
        lis.join()
