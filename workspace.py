from tkinter import Tk, Canvas, Frame
from abc import ABC, abstractmethod

class Workspace(ABC):
    def __init__(self):
        self._window = Tk()
        self._title = "Workspace"
        self._width = 500
        self._height = 500
        self._center = [0, 0]
        self._basis = [1, 1]
        self._canvas = None
        self._color = "white"
        self._play = True # Mude o valor dessa variável para pausar o sistema
        self._time = 50
        self._drawings = [] # Guardará os desenhos feitos em cada ciclo para serem apagados no próximo 

        self.__setup()

        self._window.mainloop()

    @abstractmethod
    def config(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    def set_title(self, title):
        self._title = title

    def set_time(self, time):
        self._time = time

    def set_fps(self, fps):
        self._time = int(1000/fps)

    def stop(self):
        self._play = False

    def play(self):
        self._play = True

    def bind(self, str, func):
        self._window.bind(str, func)

    def size(self, width, height):
        self._width = width
        self._height = height

    # Variáveis "perm" definem se o objeto desenhado vai ser apagado em cada update ou não
    def line(self, x1, y1, x2, y2, perm = False, **kwargs):
        if not perm:
            self._drawings.append(self._canvas.create_line(self.coord(x1, 0), self.coord(y1, 1), self.coord(x2, 0), self.coord(y2, 1), **kwargs))
        else:
            self._canvas.create_line(self.coord(x1, 0), self.coord(y1, 1), self.coord(x2, 0), self.coord(y2, 1), **kwargs)

    def circle(self, x, y, a, b, perm = False, **kwargs):
        if not perm:
            self._drawings.append(self._canvas.create_oval(self.coord(x-a, 0), self.coord(y-b, 1), self.coord(x+a, 0), self.coord(y+b, 1), **kwargs))
        else:
            self._canvas.create_oval(self.coord(x-a, 0), self.coord(y-b, 1), self.coord(x+a, 0), self.coord(y+b, 1), **kwargs)

    # Mudar o sistema de coordenadas que por padrão tem o centro no canto superior esquerdo e tem o eixo y invertido
    # Para ter um sistema cartesiano padrão use coord_sys(self._width/2, self._height/2, 1, -1)
    def coord_sys(self, x, y, e1 = 1, e2 = 1): 
        self._center = [x, y]
        self._basis = [e1, e2]

    # Conversões
    # Coordenadas no sistema definido para coordenadas em pixels. id = 0 para x 1 para y
    def coord(self, num, id):
        return self._center[id] + num*self._basis[id]

    # Coordenadas em pixels para coordenadas no sistema definido. id = 0 para x 1 para y
    def _coord(self, num, id):
        return (num - self._center[id])/self._basis[id]

    def __setup(self):
        self.config()

        self._window.geometry('%ix%i' % (self._width, self._height))
        self._window.resizable(False, False)
        self._window.title(self._title)

        frame = Frame(bg=self._color)
        frame.pack()

        self._canvas = Canvas(frame, width=self._width, height=self._height, bg=self._color)
        self._canvas.pack()

        self.__update()

    def __update(self):
        if self._play:
            # Apaga todos os desenhos do último ciclo
            for i in self._drawings:
                self._canvas.delete(i)
            self._drawings.clear()

            # Desenha novamente
            self.draw()

        # Mantém em loop o método __update()
        self._window.after(self._time, self.__update)

    
