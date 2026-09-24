import pygame #1- Importa a biblioteca do pygame. 
from pygame.locals import * #2- Importa todas as constantes do módulo locals do pygame
from sys import exit #3- Importa a função exit do módulo sys

pygame.init() #4- Inicializa todos os módulos do pygame

Largura = 640
Altura = 480 

tela = pygame.display.set_mode((Largura, Altura)) #5- Cria uma janela com tamanho definido pelas variáveis
pygame.display.set_caption("Jogo de Teste") #5.A- Define o título da janela

while True: #6- Loop principal do jogo
    for event in pygame.event.get(): #7- Loop para capturar eventos do pygame
        if event.type == QUIT: # 7.A- Verifica se o evento é do tipo QUIT (fechar a janela)
            pygame.quit() # 7.B- Encerra todos os módulos do pygame
            exit() # 7.C- Sai do programa

        pygame.draw.rect(tela, (255, 0, 0), (200, 300, 40, 50)) # 8- Desenha um retângulo vermelho na tela. O primeiro parêntese define a superfície onde o retângulo será desenhado (tela), o segundo define a cor (vermelho) através de uma tupla de valores RGB(255 de vermelho, 0 de verde, 0 de azul), e o terceiro define a posição e tamanho do retângulo (x[que representa a coordenada x no plano cartesiano], y[no plano cartesiano], largura do retângulo, altura do retângulo).
        pygame.draw.circle(tela, (0, 255, 0), (300, 260), 40) # 9- Desenha um círculo verde na tela. Ele define a cor verde pelos valores RGB(0 red, 255 green, 0 blue),  o número após o parêntese de posicionamento do formato define o raio do círculo.
        pygame.draw.line(tela, (0, 0, 255), (390, 0), (390, 600), 5) # 10- Desenha uma linha azul na tela. O terceiro parêntese define o ponto inicial da linha (x1, y1), o quarto define o ponto final da linha (x2, y2) e o último número define a espessura da linha.

        pygame.display.update() #Atualiza o conteúdo da janela
