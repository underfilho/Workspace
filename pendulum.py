from workspace import Workspace
import math

class Main(Workspace):
    def __init__(self):
        self.ang = math.pi/4 # Angulo do pêndulo
        self.ang_ = 0 # Velocidade angular
        self.ang__ = 0 # Aceleração angular
        self.len = 150 # Tamanho do fio
        super().__init__()

    def config(self):
        self._title = "Pendulum"
        self.size(300, 250)
        self.coord_sys(150, 50)
        self._time = 30

    def draw(self):
        ball = [self.len*math.sin(self.ang), self.len*math.cos(self.ang)] # Posição da bola
        self.line(0, 0, ball[0], ball[1], fill="black")
        self.circle(ball[0], ball[1], 10, 10, fill="black") # Círculo de raio 10

        self.ang__ = -1*math.sin(self.ang)/self.len # Equação de aceleração do pêndulo simples com g=1
        self.ang_ += self.ang__ 
        self.ang += self.ang_

if __name__ == "__main__":
    Main()