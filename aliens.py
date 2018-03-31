import random
import threading
from math import *
from board import *


# Aliens Class
class aliens:
        def __init__(self, r):
                self.r = r
                threading.Timer(8, self.destruct).start()
                board1.space[1 + r / 10][1 + r % 8] = "$"

        @staticmethod
        def spawn():
                threading.Timer(10, aliens.spawn).start()
                r = random.randrange(16)
                while(board1.space[1 + r / 10][1 + r % 8] != " "):
                        r = random.randrange(16)
                aliens(r)

        def destruct(self):
                r = self.r
                if(board1.space[1 + r / 10][1 + r % 8] == '$'):
                        board1.space[1 + r / 10][1 + r % 8] = " "


