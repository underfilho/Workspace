from workspace import Workspace 
import math

class Main(Workspace):
    def __init__(self):
        self.ang = math.pi/4 # Angulo do pêndulo
        self.ang_ = 0 # Velocidade angular
        self.ang__ = 0 # Aceleração angular
        self.len = 150 # Tamanho do fio
        super().__init__()

    def config(self): # Configurações
        self.set_title("Pendulum")
        self.size(300, 250)
        self.coord_sys(150, 50) # Define o centro (0, 0)
        self.set_fps(30) # Define o numero de frames por segundo

    def draw(self): # Método que será chamado a cada frame sobrescrevendo o último draw
        ball = [self.len*math.sin(self.ang), self.len*math.cos(self.ang)] # Posição da bola
        self.line(0, 0, ball[0], ball[1], fill="black") # Desenha o fio
        self.circle(ball[0], ball[1], 10, 10, fill="black") # Desenha um círculo de raio 10

        self.ang__ = -1.5*math.sin(self.ang)/self.len # Equação de aceleração do pêndulo simples com g=1.5
        self.ang_ += self.ang__ 
        self.ang += self.ang_

if __name__ == "__main__":
    Main()