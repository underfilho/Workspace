# Workspace
Biblioteca Python para a criação de desenhos e sistemas físicos.
Baseado em https://processing.org/

Como exemplos do uso da biblioteca, [arrow.py](https://github.com/underfilho/Workspace/blob/master/arrow.py) é o exemplo mais simples e iniciante, uma simples setinha batendo nas bordas que muda sua posição no clique.

<img src="https://user-images.githubusercontent.com/31104317/130129026-bfa9a34c-42e6-48ce-a125-623540001912.gif" width="40%" height="40%"/>

Já [pendulum.py](https://github.com/underfilho/Workspace/blob/master/pendulum.py) simula um [pêndulo simples](https://en.wikipedia.org/wiki/Pendulum_(mathematics)) fisicamente usando menos de 30 linhas de código.

<img src="https://user-images.githubusercontent.com/31104317/130129378-23d4bab6-16f9-4bc4-b1e9-5a72780d10dc.gif" width="40%" height="40%"/>

E por último [simple_snake.py](https://github.com/underfilho/Workspace/blob/master/simple_snake.py) cria o famoso jogo da cobrinha, esse utilizando apenas 50 linha de código.

<img src="https://user-images.githubusercontent.com/31104317/130129498-c1fdf9ac-9cd2-4e67-ab89-7c1f30944dad.gif" width="40%" height="40%"/>

# Como usar
Primeiro baixe [Workspace.py](https://github.com/underfilho/Workspace/blob/master/workspace.py) na sua pasta do projeto e importe, depois você deve criar sua classe como filha de Workspace, no método __init__ crie suas variáveis (como posições e velocidades), não esqueça de chamar o ```super().__init__()```, config e draw são métodos abstratos, então você deve sobrescrevê-los
``` 
class MyClass(Workspace):
  def __init__(self):
    # Suas variáveis...
    super().__init__()
    
  def config(self):
    # Suas configurações...
    
  def draw(self): # Método chamado a cada frame, apagando os desenhos anteriores (exceto se especificado pra não apagar)
    # Seus desenhos e manipulações das variáveis...
    
```

# Configurações

```self.set_title("Titulo")``` Define o titulo da janela.

```self.size(width, height)``` Define o tamanho da janela.

```self.coord_sys(center_x, center_y, e1: base_e1, e2: base_e2)``` Explico melhor a seguir.

```self.set_time(20)``` Primeira opção de determinar o tempo, a cada 20 milissegundos draw é chamada novamente e um novo frame gerado.

```self.set_fps(30)``` Segunda opção de definir o tempo (aproximadamente 30 frames por segundo, pois ao converter pra int acaba perdendo precisão).

```self.bind("<Return>", funcao)``` Cria um evento pra quando a tecla em questão for pressionada.
    
    
# Desenhos

Os desenhos usam a class Vector de workspace.py como argumentos para facilitar.

```self.line(ponto_inicial, ponto_final, permanencia, fill="blue")``` Desenha uma linha com os pontos em questão (Vetores da classe Vector em workspace.py), permanência é um argumento bool opcional, caso True o desenho não será apagado nos próximos frames, argumentos extras também são possíveis, nesse caso a linha será azul. (Permanência e argumentos adicionais estão disponíveis para todos os desenhos).

```self.circle(centro, a, b, fill="black")``` Desenha uma elipse, a e b são numerps, caso queira realmente um círculo dê o mesmo valor para a e b, sendo assim, o raio do círculo, em fill você pode definir a cor (assim como para self.line).

```self.rec(centro, largura, altura)``` e ```self.rec_corners(superior_esquerdo, inferior_direito)``` Desenham retângulos, rec baseado no centro e rec_corners usando dois pontos, superior esquerdo e inferior direito.

Com ```self.stop()``` e ```self.play()``` é possível pausar e dar play novamente no ciclo.

Para conhecer mais argumentos extras http://www.effbot.org/tkinterbook/canvas.htm (self.line envia todos os argumentos extras para canvas.create_line, assim como circle para create_oval)

# Sistema de coordenadas

Por padrão o canvas do Tkinter tem seu centro (0,0) na borda superior esquerda, então o eixo x tem valores positivos para a direita e o eixo y tem valores positivos para baixo, caso você queira mudar isso você pode definir o novo centro e se quiser também pode inverter o eixo y, usando -1 como base e2. Caso queira um eixo cartesiano padrão apenas use ```self.coord_sys(width/2, height/2, 1, -1)```

# Eventos e bindings

Valor de cada tecla pode ser encontrado aqui https://web.archive.org/web/20190515021108id_/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html ou http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm

# Sugestões

Várias das ideias que tive tirei dessa playlist https://www.youtube.com/playlist?list=PLRqwX-V7Uu6ZiZxtDDRCi6uhfTH4FilpH, ele usa Processing, mas o funcionamento é quase o mesmo, já que me baseei nessa biblioteca, um exemplo ótimo pra iniciar é tentar fazer o jogo da cobrinha, que ele também explica nesse vídeo https://www.youtube.com/watch?v=AaGK-fj-BAM
