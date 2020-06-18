from tkinter import Tk, Canvas, Frame
from abc import ABC, abstractmethod

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def times(self, num):
        return Vector(self.x * num, self.y * num)

    def xy(self):
        return (self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def equal(self, other):
        return self.x == other.x and self.y == other.y

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

        self._setup()

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
    def line(self, start, end, perm = False, **kwargs):
        x1, y1 = start.xy()
        x2, y2 = end.xy()
        if not perm:
            self._drawings.append(self._canvas.create_line(self.systopx(x1, 0), self.systopx(y1, 1), self.systopx(x2, 0), self.systopx(y2, 1), **kwargs))
        else:
            self._canvas.create_line(self.systopx(x1, 0), self.systopx(y1, 1), self.systopx(x2, 0), self.systopx(y2, 1), **kwargs)

    def circle(self, center, a, b, perm = False, **kwargs):
        x, y = center.xy()
        if not perm:
            self._drawings.append(self._canvas.create_oval(self.systopx(x-a, 0), self.systopx(y-b, 1), self.systopx(x+a, 0), self.systopx(y+b, 1), **kwargs))
        else:
            self._canvas.create_oval(self.systopx(x-a, 0), self.systopx(y-b, 1), self.systopx(x+a, 0), self.systopx(y+b, 1), **kwargs)

    def rec(self, center, width, height, perm = False, **kwargs):
        x, y = center.xy()
        a = width/2
        b = height/2
        if not perm:
            self._drawings.append(self._canvas.create_rectangle(self.systopx(x-a, 0), self.systopx(y-b, 1), self.systopx(x+a, 0), self.systopx(y+b, 1), **kwargs))
        else:
            self._canvas.create_rectangle(self.systopx(x-a, 0), self.systopx(y-b, 1), self.systopx(x+a, 0), self.systopx(y+b, 1), **kwargs)

    def rec_corners(self, topleft, rightbot, perm = False, **kwargs):
        x1, y1 = topleft.xy()
        x2, y2 = rightbot.xy()
        if not perm:
            self._drawings.append(self._canvas.create_rectangle(self.systopx(x1, 0), self.systopx(y1, 1), self.systopx(x2, 0), self.systopx(y2, 1), **kwargs))
        else:
            self._canvas.create_rectangle(self.systopx(x1, 0), self.systopx(y1, 1), self.systopx(x2, 0), self.systopx(y2, 1), **kwargs)

    # Mudar o sistema de coordenadas que por padrão tem o centro no canto superior esquerdo e tem o eixo y invertido
    # Para ter um sistema cartesiano padrão use coord_sys(self._width/2, self._height/2, 1, -1)
    def coord_sys(self, x, y, e1 = 1, e2 = 1): 
        self._center = [x, y]
        self._basis = [e1, e2]

    # Conversões
    # Coordenadas no sistema definido para coordenadas em pixels. id = 0 para x e id = 1 para y
    def systopx(self, num, id):
        return self._center[id] + num*self._basis[id]

    # Coordenadas em pixels para coordenadas no sistema definido. id = 0 para x e id = 1 para y
    def pxtosys(self, num, id):
        return (num - self._center[id])/self._basis[id]

    def _setup(self):
        self.config()

        self._window.geometry('%ix%i' % (self._width, self._height))
        self._window.resizable(False, False)
        self._window.title(self._title)

        frame = Frame(bg=self._color)
        frame.pack()

        self._canvas = Canvas(frame, width=self._width, height=self._height, bg=self._color, highlightthickness=0)
        self._canvas.pack()

        self._update()

    def _update(self):
        if self._play:
            # Apaga todos os desenhos do último ciclo
            for i in self._drawings:
                self._canvas.delete(i)
            self._drawings.clear()

            # Desenha novamente
            self.draw()

        # Mantém em loop o método _update()
        self._window.after(self._time, self._update)