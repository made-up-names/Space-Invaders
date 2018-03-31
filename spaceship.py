from board import *

# Spaceship Class
class spaceship:
        def __init__(self, r, c):
                self.r = r
                self.c = c
                board1.space[r][c] = "A"

        def moveleft(self):
                if(self.c != 1):
                        board1.space[self.r][self.c] = " "
                        board1.space[self.r][self.c - 1] = "A"
                        self.c = self.c - 1

        def moveright(self):
                if(self.c != 8):
                        board1.space[self.r][self.c] = " "
                        board1.space[self.r][self.c + 1] = "A"
                        self.c = self.c + 1

