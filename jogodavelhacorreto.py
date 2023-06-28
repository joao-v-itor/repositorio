import pygame
import sys

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
COR_X = (255, 0, 0)
COR_O = (0, 0, 255)

# Dimensões da janela
largura_janela = 300
altura_janela = 400

# Dimensões do tabuleiro
tamanho_quadrado = 100
espessura_linha = 4

# Inicializar o Pygame
pygame.init()

# Configurar a janela
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Jogo da Velha")

def exibir_tabuleiro(tabuleiro):
    janela.fill(BRANCO)

    for linha in range(3):
        for coluna in range(3):
            pygame.draw.rect(janela, PRETO, (coluna * tamanho_quadrado, linha * tamanho_quadrado, tamanho_quadrado, tamanho_quadrado), espessura_linha)
            if tabuleiro[linha][coluna] != " ":
                if tabuleiro[linha][coluna] == "X":
                    cor_simbolo = COR_X
                else:
                    cor_simbolo = COR_O
                fonte = pygame.font.Font(None, 120)
                texto = fonte.render(tabuleiro[linha][coluna], True, cor_simbolo)
                posicao_texto = texto.get_rect(center=(coluna * tamanho_quadrado + tamanho_quadrado/2, linha * tamanho_quadrado + tamanho_quadrado/2))
                janela.blit(texto, posicao_texto)

    pygame.display.update()

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(posicao == jogador for posicao in linha):
            return True

    # Verificar colunas
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

def exibir_mensagem_vencedor(vencedor):
    janela.fill(BRANCO)
    fonte = pygame.font.Font(None, 48)
    texto = fonte.render("Vencedor: " + vencedor, True, PRETO)
    posicao_texto = texto.get_rect(center=(largura_janela / 2, altura_janela / 2))
    janela.blit(texto, posicao_texto)
    pygame.display.update()

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogo_em_andamento = True
    vencedor = None

    while jogo_em_andamento:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and jogo_em_andamento:
                posicao_mouse = pygame.mouse.get_pos()
                coluna = posicao_mouse[0] // tamanho_quadrado
                linha = posicao_mouse[1] // tamanho_quadrado

                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = jogador_atual

                    if verificar_vitoria(tabuleiro, jogador_atual):
                        vencedor = jogador_atual
                        jogo_em_andamento = False
                    elif all(posicao != " " for linha in tabuleiro for posicao in linha):
                        vencedor = "Empate"
                        jogo_em_andamento = False
                    else:
                        jogador_atual = "O" if jogador_atual == "X" else "X"

        exibir_tabuleiro(tabuleiro)

    if vencedor:
        exibir_mensagem_vencedor(vencedor)

        
        aguardando_clique = True
        while aguardando_clique:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    aguardando_clique = False

jogar_jogo_da_velha()








