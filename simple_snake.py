from workspace import *
from random import randint

class SimpleSnake(Workspace):
    def __init__(self):
        self.positions = [Vector(1, 1)]
        self.directions = { 1: Vector(1, 0), -1: Vector(-1, 0), 2: Vector(0, 1), -2: Vector(0, -1) }
        self.direction = 1
        self.food = None
        super().__init__()

    def config(self):
        self.set_title("Snake")
        self.size(300, 300)
        self.coord_sys(0, 0, 10, 10)
        self.set_fps(5)
        self.bind("<Right>", lambda e: self.set_direction(1))
        self.bind("<Left>", lambda e: self.set_direction(-1))
        self.bind("<Down>", lambda e: self.set_direction(2))
        self.bind("<Up>", lambda e: self.set_direction(-2))

    def draw(self):
        if(self.food == None):
            self.food = Vector(randint(1, 29), randint(1, 29))

        for i in range(1, len(self.positions)):
            self.positions[-i] = self.positions[-i-1]
        self.positions[0] = self.positions[0] + self.directions[self.direction]

        self.rec_corners(self.food.x, self.food.y, self.food.x+1, self.food.y+1, fill="red")
        for i in self.positions:
            self.rec_corners(i.x, i.y, i.x+1, i.y+1, fill="black")
        
        if(self.positions[0].equal(self.food)):
            self.new_cell()
            self.food = None

    def set_direction(self, dir):
        if dir != -self.direction:
            self.direction = dir

    def new_cell(self):
        last = self.positions[-1]
        self.positions.append(last)
  
if __name__ == "__main__":
    SimpleSnake()        