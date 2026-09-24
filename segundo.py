import pygame
from pygame.locals import *
from sys import exit

pygame.init()

Largura = 640
Altura = 480
x = Largura // 2 # Posição inicial do retângulo no eixo X, que é definida como a metade da largura da janela, centralizando o retângulo horizontalmente.
y = 0 # Posição inicial do retângulo no eixo Y, que é definida como 0, colocando o retângulo no topo da janela.
tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption("Jogo de Teste")
relogio = pygame.time.Clock() # Cria um objeto Clock para controlar a taxa de atualização do jogo.

while True:
    relogio.tick(60) # Define a taxa de atualização do jogo para 60 quadros por segundo (FPS), garantindo que o loop principal seja executado a uma velocidade constante.
    tela.fill((0, 0, 0)) # Preenche a tela com a cor preta a cada iteração do loop, limpando o conteúdo anterior.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50)) # Nesse retângulo, a posição inicial é definida pelas variáveis x e y, que são atualizadas a cada iteração do loop.
    if y >= Altura: # Verifica se o retângulo saiu da tela (ou seja, se a coordenada y é maior ou igual que a altura da janela).
        y = 0 # Reinicia a posição y para o topo da tela.
    y = y + 5 # A cada iteração do loop, a variável y é incrementada em 5, fazendo com que o retângulo se mova para baixo na tela. Isso cria a ilusão de movimento, já que o retângulo é redesenhado em uma posição diferente a cada quadro.


    pygame.display.update()