# Workspace
"Biblioteca" Python para a criação de desenhos e sistemas físicos.
Baseado em https://processing.org/

arrow.py e pendulum.py servem como simples exemplos do uso da biblioteca

# Como usar

Primeiro de tudo você deve criar sua classe como filha de Workspace, no método __init__ crie suas variáveis, como posições e velocidades (não esqueça de chamar o super().__init__), config e draw são métodos abstratos, então você deve sobrescrevê-los
``` 
class MyClass(Workspace):
  def __init__(self):
    suas variáveis...
    super().__init__()
    
  def config(self):
    self.set_title("Titulo") # Titulo da janela
    self.size(width, height) # Define o tamanho da janela
    self.coord_sys(center_x, center_y, e1: base_e1, e2: base_e2) # Explico melhor a seguir
    self.set_time(20) # a cada 20 milissegundos draw é chamada novamente e um novo frame gerado 
    self.set_fps(30) # outra opção de definir o tempo (aproximadamente 30 frames por segundo, pois por converter pra int acaba perdendo precisão)
    self.bind("<Return>", funcao) # Cria um evento pra quando a tecla em questão for pressionada (valor de cada tecla pode ser encontrado aqui https://web.archive.org/web/20190515021108id_/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html)
    
  def draw(self): # Método chamado a cada frame, apagando os desenhos anteriores (exceto se especificado pra não apagar)
    self.line(x1, y1, x2, y2, permanencia) # Desenha uma linha, permanencia é um argumento opcional, caso queira que a linha não seja apagada apenas envie esse argumento como True
    self.circle(center_x, center_y, largura, altura, fill="black") # Desenha uma elipse*, caso queira realmente um círculo dê o mesmo valor para largura e altura, sendo assim o raio do círculo, em fill você pode definir a cor (assim como para self.line)
    
    # Essa é a parte que você é livre e deve brincar com os valores, mudando a cada ciclo as variáveis posição, velocidade, etc criadas em init, ou o que você quiser fazer, ainda falta adicionar alguns métodos de desenho, mas pretendo fazer isso logo
```

# Sistema de coordenadas

Por padrão o canvas do Tkinter tem seu centro (0,0) na borda superior esquerda, então o eixo x tem valores positivos para a direita e o eixo y tem valores positivos para baixo, caso você queira mudar isso você pode definir o novo centro e se quiser também pode inverter o eixo y, usando -1 como base e2. Caso queira um eixo cartesiano padrão apenas use ```self.coord_sys(width/2, height/2, 1, -1)```

# Sugestões

Várias das ideias que tive tirei dessa playlist https://www.youtube.com/playlist?list=PLRqwX-V7Uu6ZiZxtDDRCi6uhfTH4FilpH, ele usa Processing, mas o funcionamento é quase o mesmo, já que me baseei nessa biblioteca, um exemplo ótimo pra iniciar é tentar fazer o jogo da cobrinha, que ele também explica nesse vídeo https://www.youtube.com/watch?v=AaGK-fj-BAM
