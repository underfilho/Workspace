from tkinter import Tk, Canvas, Frame

class Workspace:
    def __init__(self):
        self._window = Tk()
        self.title = "Workspace"
        self.width = 500
        self.height = 500
        self.center = [0, 0]
        self.basis = [1, 1]
        self.canvas = None
        self.color = "white"
        self.play = True # Mude o valor dessa variável para pausar o sistema
        self.time = 50
        self.drawings = [] # Guardará os desenhos feitos em cada ciclo para serem apagados no próximo 

        self.setup()

        self._window.mainloop()

    def setup(self):
        self.config()

        self._window.geometry('%ix%i' % (self.width, self.height))
        self._window.resizable(False, False)
        self._window.title(self.title)

        frame = Frame(bg=self.color)
        frame.pack()

        self.canvas = Canvas(frame, width=self.width, height=self.height, bg=self.color)
        self.canvas.pack()

        self.__update()

    def size(self, width, height):
        self.width = width
        self.height = height

    # Variáveis "perm" definem se o objeto desenhado vai ser apagado em cada update ou não
    def line(self, x1, y1, x2, y2, perm = False, **kwargs):
        if not perm:
            self.drawings.append(self.canvas.create_line(self.coord(x1, 0), self.coord(y1, 1), self.coord(x2, 0), self.coord(y2, 1), **kwargs))
        else:
            self.canvas.create_line(self.coord(x1, 0), self.coord(y1, 1), self.coord(x2, 0), self.coord(y2, 1), **kwargs)

    def circle(self, x, y, a, b, perm = False, **kwargs):
        if not perm:
            self.drawings.append(self.canvas.create_oval(self.coord(x-a, 0), self.coord(y-b, 1), self.coord(x+a, 0), self.coord(y+b, 1), **kwargs))
        else:
            self.canvas.create_oval(self.coord(x-a, 0), self.coord(y-b, 1), self.coord(x+a, 0), self.coord(y+b, 1), **kwargs)

    def coord_sys(self, x, y, e1 = 1, e2 = 1):
        self.center = [x, y]
        self.basis = [e1, e2]

    def coord(self, num, id):
        return self.center[id] + num*self.basis[id]

    def _coord(self, num, id):
        return (num - self.center[id])/self.basis[id]

    def __update(self):
        if self.play:
            # Apaga todos os desenhos do último ciclo
            for i in self.drawings:
                self.canvas.delete(i)
            self.drawings.clear()

            # Desenha novamente
            self.draw()

        # Mantém em loop
        self._window.after(self.time, self.__update)
