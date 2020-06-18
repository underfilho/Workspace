from tkinter import LAST
from workspace import *

class Main(Workspace):
    def __init__(self):
        self.position = Vector(10, 10) # Posição da flecha
        self.velocity = Vector(2, 2) # Velocidade em pixels por frame
        super().__init__()

    def config(self):
        self.set_title("Arrow")
        self.size(400, 300)
        self.set_time(20) # A cada 20 milissegundos um novo frame é gerado
        self.bind('<Button-1>', self.newpos) # Botão esquerdo do mouse

    def draw(self):
        self.line(self.position, self.position + self.velocity, fill="black", arrow=LAST)
        self.position += self.velocity # Velocidade é adicionada a posição em cada frame

        # Se bater em alguma pareda inverta a velocidade
        if self.position.x >= 395 or self.position.x <= 5:
            self.velocity.x = -self.velocity.x
        if self.position.y >= 295 or self.position.y <= 5:
            self.velocity.y = -self.velocity.y
    
    def newpos(self, event):
        self.position = Vector(event.x, event.y)
        
if __name__ == "__main__":
    Main()