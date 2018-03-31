import time
import threading
from board import *

# Missiles Parent CLass
class missiles:
        def __init__(self, r, c):
                self.r = r
                self.c = c


class mis1(missiles):
        def __init__(self, r, c):
		self.init = r
                self.r = r
                self.c = c
                missiles.__init__(self, r, c)
                self.inc1()

        def inc1(self):
                mis1.x = threading.Timer(1, self.inc1)
                mis1.x.start()
                if(board1.space[self.r - 1][self.c] == '$'):
                        board1.score = board1.score + 1
                        board1.space[self.r][self.c] = " "
                        board1.space[self.r - 1][self.c] = "i"
                        self.r = self.r - 1

                elif(self.r <= 1):
                        mis1.x.cancel()
                        board1.space[self.r][self.c] = " "

                elif(self.r > 1):
                        if(self.init != self.r):
                                board1.space[self.r][self.c] = " "
                        board1.space[self.r - 1][self.c] = "i"
                        self.r = self.r - 1


class mis2(missiles):
        def __init__(self, r, c):
		self.init = r
                self.r = r
                self.c = c
                missiles.__init__(self, r, c)
                self.inc2()

        def inc2(self):
                mis2.x = threading.Timer(1 / 2.0, self.inc2)
                mis2.x.start()

                if(self.r <= 1):
                        mis2.x.cancel()
                        if(board1.space[self.r][self.c] != 'Q'):
                                board1.space[self.r][self.c] = " "
                elif(self.r > 1):
                    if(self.init != self.r and
                            board1.space[self.r][self.c] != 'Q'):
                            board1.space[self.r][self.c] = " "
                    if(board1.space[self.r-1][self.c] != 'Q'):
                            board1.space[self.r - 1][self.c] = "I"
                    self.r = self.r - 1
                    time.sleep(0.05)
                    if(board1.space[self.r - 1][self.c] == '$'):
                            board1.space[self.r - 1][self.c] = "Q"

                            def destroy(r, c):
                                    board1.space[r][c] = " "
                                    board1.score = board1.score + 1
                            t = threading.Timer(5, destroy,
                                                [self.r - 1, self.c])
                            t.start()

