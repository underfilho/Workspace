from workspace import Workspace
from tkinter import LAST

class Main(Workspace):
    def __init__(self):
        self.x = 10
        self.y = 10
        # Velocidades
        self.xv = 2
        self.yv = 2
        super().__init__()

    def config(self):
        self.set_title("Arrow")
        self.size(400, 300)
        self.set_time(20)
        self.bind('<Button-1>', self.newpos)

    def draw(self):
        self.line(self.x, self.y, self.x + self.xv, self.y + self.yv, fill="black", arrow=LAST)
        self.x += self.xv
        self.y += self.yv

        # Se bater em alguma pareda inverta a velocidade
        if self.x >= 395 or self.x <= 5:
            self.xv = -self.xv
        if self.y >= 295 or self.y <= 5:
            self.yv = -self.yv
    
    def newpos(self, event):
        self.x = event.x
        self.y = event.y
        
if __name__ == "__main__":
    Main()