from time import sleep
import os
import platform
from termcolor import colored
class Triangle:
    def __init__(self, height, color):
        self.height = height
        self.color = color

    # def draw(self):
    #     for i in range(1, self\.height + 1):
    #         print(' ' * (self.height - i) + '* ' * i)

    def draw_move(self, n=0):
        for i in range(1, self.height + 1):
            print(colored(' ' * n + ' ' * (self.height - i) + '* ' * i, self.color))

    def clear_console(self):
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux':
            os.system('clear')

triangle = Triangle(5, 'green')

triangle.draw_move()
sleep(2)
for i in range(3, 42, 3):
    triangle.clear_console()
    triangle.draw_move(i)
    sleep(2)