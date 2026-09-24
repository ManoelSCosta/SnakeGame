import pygame
from pygame.locals import *
from sys import exit

pygame.init()

Largura = 640
Altura = 480
x = Largura // 2
y = 0

x2_inicial = int(Largura * 0.50) # Define a posição inicial do círculo no eixo X, calculando 25% da largura da tela.
y2_inicial = Altura // 2

x2 = x2_inicial
y2 = y2_inicial

tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption("Jogo de Teste")
relogio = pygame.time.Clock()

velocidade = 3 # Define a velocidade de movimento do círculo, para atualizar sua posição com base nas teclas pressionadas pelo jogador.

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN: # Verifica se uma tecla foi pressionada. o KEYDOWN é um evento que pede ao usuário para pressionar uma tecla e executa uma ação quando isso acontece, porém, se a tecla for liberada, o evento KEYUP é acionado. Isso significa que o código dentro desse bloco será executado apenas e apenas no momento que a tecla for pressionada.
            if event.key == K_ESCAPE: # Verifica se a tecla pressionada é a tecla "ESC". Se for, o jogo será encerrado.
                pygame.quit()
                exit()
            if event.key == K_SPACE: # Verifica se a tecla pressionada é a tecla "SPACE". Se for, o círculo será reposicionado para sua posição inicial.
                x2 = x2_inicial
                y2 = y2_inicial

    teclas = pygame.key.get_pressed() # Armazena o estado atual de todas as teclas do teclado, permitindo verificar quais teclas estão sendo pressionadas pelo jogador durante o loop principal do jogo.
    if teclas[K_a] or teclas[K_LEFT]: # Verifica se a tecla "A" ou a seta para a esquerda está sendo pressionada.
        x2 -= velocidade # Atualiza a posição do círculo no eixo X, movendo-o para a esquerda com base na velocidade definida.
    if teclas[K_d] or teclas[K_RIGHT]:
        x2 += velocidade
    if teclas[K_w] or teclas[K_UP]:
        y2 -= velocidade
    if teclas[K_s] or teclas[K_DOWN]:
        y2 += velocidade
    #faJFLASDJFALSDJFLADSKJFALSDJFAÇLJFLKJLÇSDJF

    x2 = max(0, min(Largura, x2)) # Garante que a posição do círculo no eixo X permaneça dentro dos limites da tela, evitando que ele saia da área visível. Os parênteses da função "min" limitam o valor máximo de x2 à largura da tela, enquanto a função "max" garante que o valor mínimo seja 0.
    y2 = max(0, min(Altura, y2)) # "max" é uma função que retorna o maior valor entre os dois argumentos fornecidos. Neste caso, ela garante que a posição do círculo no eixo Y não seja menor que 0, mantendo-o dentro da tela. "min" é uma função que retorna o menor valor entre os dois argumentos fornecidos, garantindo que a posição do círculo no eixo Y não ultrapasse a altura da tela.
    pygame.draw.circle(tela, (0, 255, 0), (x2, y2), 20) # Desenha um círculo verde na tela com raio de 20 pixels, centralizado na posição (x2, y2).

    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    if y >= Altura:
        y = 0
    y += 5

    pygame.display.update()