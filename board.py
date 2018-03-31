import sys
import threading


# Board Class
class board1:
        score = 0
        space = []
        time = [0]
        for i in range(10):
                space.append([])
        for j in (0, 9):
                space[j].append(" ")
                for i in range(8):
                        space[j].append("_")
                space[j].append(" ")
        for j in range(1, 9):
                space[j].append("|")
                for i in range(1, 9):
                        space[j].append(" ")
                space[j].append("|")

        @staticmethod
        def printboard():
                if(board1.time[0] != 0):
                        sys.stdout.write("\033[F"*11)
                for i in range(10):
                        for j in range(10):
                                print board1.space[i][j],
                        print
                print " Score:          ", board1.score

        @staticmethod
        def counter():
                threading.Timer(1 / 20.0, board1.counter).start()

                board1.printboard()
                board1.time[0] = board1.time[0] + 1 / 20.0

