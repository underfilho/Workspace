from random import randint
from workspace import *

class SimpleSnake(Workspace):
    def __init__(self):
        self.positions = [Vector(1, 1)] # Array de posições para cada célula da cobra
        # Dicionário para facilitar nas direções, um número para cada direção
        self.directions = { 1: Vector(1, 0), -1: Vector(-1, 0), 2: Vector(0, 1), -2: Vector(0, -1) }
        self.direction = 1
        self.food = None
        super().__init__()

    def config(self):
        self.set_title("Snake")
        self.size(300, 300)
        # Base do sistema de coordenada e1=10 e e2=10, basicamente um sistema de coordenadas com escala 10px
        self.coord_sys(0, 0, 10, 10) 
        self.set_fps(5)
        self.bind("<Right>", lambda e: self.set_direction(1))
        self.bind("<Left>", lambda e: self.set_direction(-1))
        self.bind("<Down>", lambda e: self.set_direction(2))
        self.bind("<Up>", lambda e: self.set_direction(-2))

    def draw(self):
        if(self.food == None):
            self.food = Vector(randint(1, 29), randint(1, 29))

        # Percorre o array de posições na ordem inversa pegando a posição e igualando com a posição seguinte
        # Ex: a cauda vai pra posição da penultima célula, a penúltima pra posição da antepenultima e assim em diante
        for i in range(1, len(self.positions)):
            self.positions[-i] = self.positions[-i-1]
        
        # A cabeça da cobra soma com a direção que ela deve seguir
        self.positions[0] += self.directions[self.direction]

        self.rec_corners(self.food, self.food + Vector(1, 1), fill="red")
        for i in self.positions:
            self.rec_corners(i, i + Vector(1, 1), fill="black")
        
        if(self.positions[0].equal(self.food)):
            self.new_cell()
            self.food = None

    def set_direction(self, dir):
        if dir != -self.direction: # Impede que a cobra vire na direção inversa
            self.direction = dir

    def new_cell(self):
        last = self.positions[-1] # Nova célula fica na posição da última célula
        self.positions.append(last) # Adiciona a nova célula
  
if __name__ == "__main__":
    SimpleSnake()        