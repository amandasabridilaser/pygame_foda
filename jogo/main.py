import pygame
import random
import sys
import math
import asyncio
import platform
sys.platform
# Inicializa o PyGame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Matemático de Terror")
fonte_game_over = pygame.font.SysFont("niagarasolid", 150)  # Fonte Niagara Solid, tamanho 80
fonte_game_over1 = pygame.font.SysFont("chiller", 75)    # Fonte Chiller, tamanho 25
simbolos = pygame.font.SysFont("chiller", 25)    # Fonte Chiller, tamanho 25
# Definições de cores e fontes
BACKGROUND_COLOR = (30, 30, 30)  # Cor de fundo (cinza escuro)
BUTTON_COLOR = (34, 85, 30)  # Verde escuro para botões
HOVER_COLOR = (50, 130, 50)  # Cor do hover (verde mais claro)
TEXT_COLOR = (200, 200, 200)  # Cor do texto (cinza claro)
FONT = pygame.font.Font(None, 48)  # Fonte para os botões e símbolos
TITLE_FONT = pygame.font.Font(None, 60)  # Fonte padrão para o título

# Lista de opções de menu
menu_options = ["Jogar", "Sobre", "Creditos", "Sair"]
buttons = []

# Função para criar botões com centralização




# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Escolhas Matemáticas")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
CINZA = (128, 128, 128)

# Fonte
fonte = pygame.font.Font(None, 36)
xadrez = pygame.image.load('xadrez.jpg')
cena3 = pygame.image.load('cena3.jpg')
fundo1 = pygame.image.load('fundo 1.jpg')
fundo2 = pygame.image.load('fundo2.jpg')
cena1_1 = pygame.image.load('cena1.1.png')
cena1_2 = pygame.image.load('cena1.2.png')
cena1_3 = pygame.image.load('cena1_3.png')
cena2_2 = pygame.image.load('cena2_2.png')
cena2_1 = pygame.image.load('cena2_1.png')
cena2_3 = pygame.image.load('cena2_3.png')
cena3_1 = pygame.image.load('cena3_1.png')
cena3_2 = pygame.image.load('cena3_2.png')
cena3_3 = pygame.image.load('cena3_3.png')
cena4_2 = pygame.image.load('cena4_2.png')
cena4_1 = pygame.image.load('cena4_1.png')
cena4_3 = pygame.image.load('cena4_3.png')
cena4_4 = pygame.image.load('cena4_4.png')
cena4_5 = pygame.image.load('cena4_5.png')
cena4_6 = pygame.image.load('cena4_6.png')
cena4_7 = pygame.image.load('cena4_7.png')
errada1_1 = pygame.image.load('errada1_1.png')
errada1_2 = pygame.image.load('errada1_2.png')
errada1_4 = pygame.image.load('errada1_4.png')
errada3_1 = pygame.image.load('errada3_1.png')
errada3_2 = pygame.image.load('errada3_2.png')
errada3_3 = pygame.image.load('errada3_3.png')
errada3_5 = pygame.image.load('errada3_5.png')
certa1_1 = pygame.image.load('certa1_1.png')
certa1_2 = pygame.image.load('certa1_2.png')
certa1_3 = pygame.image.load('certa1_3.png')
certa2_1 = pygame.image.load('certa2_1.png')
certa2_2 = pygame.image.load('certa2_2.png')
certa2_3 = pygame.image.load('certa2_3.png')
certa3_4 = pygame.image.load('certa3_4.png')
certa3_5 = pygame.image.load('certa3_5.png')
certa3_2 = pygame.image.load('certa3_2.png')
certa3_3 = pygame.image.load('certa3_3.png')
C1 = pygame.image.load('C1.png')
C2 = pygame.image.load('C2.png')
C3 = pygame.image.load('C3.png')
C4 = pygame.image.load('C4.png')
C5 = pygame.image.load('C5.png')
C6 = pygame.image.load('C6.png')
C7 = pygame.image.load('C7.png')
C8 = pygame.image.load('C8.png')
C9 = pygame.image.load('C9.png')
def create_button(text, y):
    text_surface = FONT.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
    button_rect = pygame.Rect(0, 0, text_rect.width + 40, text_rect.height + 20)
    button_rect.center = text_rect.center
    return {"rect": button_rect, "text": text, "text_surface": text_surface, "text_rect": text_rect}

# Cria os botões do menu
start_y = HEIGHT // 2
spacing = 80
for i, option in enumerate(menu_options):
    buttons.append(create_button(option, start_y + i * spacing))

# Função para desenhar os botões do menu
def draw_buttons():
    for button in buttons:
        color = HOVER_COLOR if button["rect"].collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
        pygame.draw.rect(screen, color, button["rect"], border_radius=10)
        screen.blit(button["text_surface"], button["text_rect"])

# Função para desenhar o título com a fonte padrão
def draw_title():
    # Desenha o título principal
   
   
    
  
    texto_game_over = fonte_game_over.render("Enigmas Mortais", True, TEXT_COLOR)
    texto_game_over1 = fonte_game_over1.render("O Portal da Matemática", True, TEXT_COLOR)

    
    # Sombra do título
    shadow_color = (10, 10, 10)
    texto_game_over2 = fonte_game_over.render("Enigmas Mortais", True, shadow_color)
    texto_game_over3 = fonte_game_over1.render("O Portal da Matemática", True, shadow_color)
    
    # Centraliza o título
    title_rect_1 = texto_game_over.get_rect(center=(WIDTH // 2, 100))
    title_rect_2 = texto_game_over1.get_rect(center=(WIDTH // 2, 220))
    
    # Centraliza a sombra ligeiramente deslocada
    shadow_offset = 4
    shadow_rect_1 = title_rect_1.move(shadow_offset, shadow_offset)
    shadow_rect_2 = title_rect_2.move(shadow_offset, shadow_offset)
    
    # Desenha a sombra e o texto do título
    screen.blit(texto_game_over2, shadow_rect_1)
    screen.blit(texto_game_over, title_rect_1)
    screen.blit(texto_game_over3, shadow_rect_2)
    screen.blit(texto_game_over1, title_rect_2)


# Função para desenhar um círculo giratório de símbolos matemáticos
def draw_symbol_circle(center_x, center_y, radius=200, angle_speed=0.002, scale=1.0):
    symbols = ["+", "√", "∑", "Δ", "π", "-", "≠", "Φ", "λ", "Ω"]
    for index, s in enumerate(symbols):
        angle = pygame.time.get_ticks() * angle_speed + index * (2 * math.pi / len(symbols))
        x = center_x + int(radius * math.cos(angle))
        y = center_y + int(radius * math.sin(angle))
        symbol_surface = FONT.render(s, True, (100, 255, 100))
        symbol_surface = pygame.transform.scale(symbol_surface, (int(symbol_surface.get_width() * scale), int(symbol_surface.get_height() * scale)))
        symbol_rect = symbol_surface.get_rect(center=(x, y))
        screen.blit(symbol_surface, symbol_rect)
def open_play_screen():
    print("Tela de jogo iniciada!")

def open_credits_screen():
    # Loop para a tela de créditos
    credits_running = True
    while credits_running:
        # Preenche o fundo da tela de créditos
        screen.fill((20, 20, 20))  # Cor de fundo mais escura para os créditos

        # Definir texto de créditos
        credit_lines = [
            "Créditos",
            "Desenvolvedores:",
            "Amanda Silva",
            "João Souza",
            "Design e Efeitos:",
            "Maria Oliveira",
            "Som e Música:",
            "Lucas Almeida",
            "Agradecimentos Especiais:",
            "Comunidade Python",
            "Pressione 'Esc' para voltar"
        ]

        # Exibe cada linha de crédito centralizada
        for i, line in enumerate(credit_lines):
            credit_text = FONT.render(line, True, (200, 200, 200))  # Texto em cinza claro
            text_rect = credit_text.get_rect(center=(WIDTH // 2, 50 + i * 50))

            screen.blit(credit_text, text_rect)

        # Atualiza a tela
        pygame.display.flip()

        # Eventos para fechar a tela de créditos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Sai da tela de créditos com 'Esc'
                    credits_running = False

def open_options_screen():
    print("Tela de créditos aberta!")
# Loop principal do jogo

    # Atualiza a tela
 
# Função para desenhar o texto na tela de forma progressiva
def desenha_texto_gradual(texto, posicao, cor=BRANCO, delay=30):
    for i in range(1, len(texto) + 1):
        # Renderiza o texto principal
        texto_surface = fonte.render(texto[:i], True, cor)
        
        # Renderiza o texto para a borda (em preto)
        borda_surface = fonte.render(texto[:i], True, PRETO)
        
        # Desenha a borda preta em volta do texto principal, deslocando em várias direções
        offsets = [(-1, -1), (1, -1), (-1, 1), (1, 1)]  # Cima-esquerda, cima-direita, baixo-esquerda, baixo-direita
        for offset in offsets:
            tela.blit(borda_surface, (posicao[0] + offset[0], posicao[1] + offset[1]))

        # Desenha o texto principal no centro
        tela.blit(texto_surface, posicao)
        
        pygame.display.flip()
        pygame.time.delay(delay)


def desenha_caixa_resposta(texto, x, y, largura, altura, cor=BRANCO):
    caixa_rect = pygame.Rect(x, y, largura, altura)
    pygame.draw.rect(tela, cor, caixa_rect, 2)
    desenha_texto(texto, (x + 10, y + 10), cor)
    return caixa_rect

def desenha_cena_com_texto(imagem, texto):
  
  
    tela.blit(imagem, (100, 0))  # Desenha a imagem de fundo
    desenha_texto_na_caixa(texto)  # Desenha o texto na caixa
    pygame.display.flip()  # Atualiza a tela
    
def desenha_cena_com_texto2(imagem_esquerda, imagem_direita, texto):
    # Desenha a imagem da esquerda (ajuste a posição conforme necessário)
    tela.blit(imagem_esquerda, (-50, 0))

    # Desenha a imagem da direita (ajuste a posição conforme necessário)
    tela.blit(imagem_direita, (250, 0))  # Assume uma tela larga o suficiente para espaçar

    desenha_texto_na_caixa(texto)  # Desenha o texto na caixa
    pygame.display.flip()  # Atualiza a tela


def desenha_texto(texto, posicao, cor=BRANCO):
    texto_surface = fonte.render(texto, True, cor)
    tela.blit(texto_surface, posicao)

# Função para quebrar o texto em várias linhas
def quebrar_texto(texto, largura_max):
    palavras = texto.split(' ')
    linhas = []
    linha_atual = ""
    
    for palavra in palavras:
        if fonte.size(linha_atual + palavra)[0] < largura_max:
            linha_atual += palavra + " "
        else:
            linhas.append(linha_atual)
            linha_atual = palavra + " "
    
    linhas.append(linha_atual)  # Adiciona a última linha
    return linhas

def reiniciar_jogo():
    # Chamando a cena inicial do jogo
    cena_inicial()
    # Reinicia o fluxo do jogo, se necessário
    jogo()  # Chama a função principal do jogo

# Função para desenhar uma caixa de diálogo na parte inferior
def desenha_caixa_dialogo():
    caixa_dialogo = pygame.Surface((largura, 150))
    
    # Define a cor do retângulo como preto
    caixa_dialogo.fill(PRETO)
    
    # Define a transparência (0 é totalmente transparente e 255 é opaco)
    caixa_dialogo.set_alpha(128)  # Ajuste 128 para mais ou menos transparência

    # Desenha o retângulo na posição desejada
    tela.blit(caixa_dialogo, (0, altura - 150))

    pygame.draw.rect(tela, BRANCO, (10, altura - 140, largura - 20, 130), 3)
def transparente():
    telas = pygame.Surface((800, 600))
    
    # Define a cor do retângulo como preto
    telas.fill(PRETO)
    
    # Define a transparência (0 é totalmente transparente e 255 é opaco)
    telas.set_alpha(128)
    tela.blit(telas, (0, 0))
# Função para desenhar o texto na caixa de diálogo com quebras automáticas
def desenha_texto_na_caixa(texto, cor=BRANCO, delay=30):
    desenha_caixa_dialogo()
    
    largura_maxima = largura - 40  
    linhas = quebrar_texto(texto, largura_maxima)
    
    # Desenha cada linha gradualmente
    y_pos = altura - 120 
    for linha in linhas:
        desenha_texto_gradual(linha.strip(), (30, y_pos), cor, delay)
        y_pos += 40  # Avança para a próxima linha
        pygame.display.flip()
        pygame.time.delay(delay)

# Função para aguardar por um clique ou tecla pressionada
def esperar_interacao():
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                esperando = False

# Função para a cena inicial

def cena_inicial():
    
    tela.blit(fundo1, (0, 0))
    desenha_cena_com_texto(cena1_1,"Você estava apenas seguindo sua rotina comum quando algo completamente inesperado acontece.")
    esperar_interacao()
    tela.fill(PRETO)
    
    tela.blit(fundo1, (0, 0))
    
    desenha_cena_com_texto(cena1_2,"No meio de uma caminhada pelo parque, você avista uma figura misteriosa, com um manto brilhante que reluz à luz do sol.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(fundo1, (0, 0))
    desenha_cena_com_texto(cena1_3 ,"Curioso, você decide segui-la e, antes que perceba, ela desaparece diante de um portal rodopiante, com símbolos matemáticos flutuando no ar.")
    esperar_interacao()
    

# Função para a segunda cena
def cena_2():
    tela.fill(PRETO)
    tela.blit(fundo2, (0, 0))
    desenha_cena_com_texto(cena2_1, "Quando voce olha a sua volta o ambiente está estranho e você vê uma figura misteriosa à sua frente.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(fundo2, (0, 0))
    desenha_cena_com_texto2(cena2_2,C1, "Figura misteriosa: Prazer em conhecê-lo, para escapar, você precisa resolver desafios matemáticos e lógicos.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(fundo2, (0, 0))
    desenha_cena_com_texto2(cena2_3,C2, "Demônio: Prepare-se, seu primeiro desafio está chegando...")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(fundo2, (0, 0))



def cena_resposta_correta():
    tela.fill(PRETO)
    tela.blit(fundo2, (0, 0))
    desenha_cena_com_texto2(certa1_1,C3,"A resposta está correta! O demônio sorri de forma maliciosa, mas desaparece num piscar de olhos.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(fundo2, (0, 0))
    desenha_cena_com_texto(certa1_2,"Uma passagem surge diante de você, e uma voz distante ecoa: 'Por enquanto, sua sabedoria te salvou... mas não se acostume.'")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(fundo2, (0, 0))
    desenha_cena_com_texto(certa1_3,"Você avança para a próxima sala.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(fundo2, (0, 0))

def cena_resposta_correta_2():
    tela.fill(PRETO)
    tela.blit(xadrez, (0, 0))
    desenha_cena_com_texto(certa2_1,"Parabéns! Você acertou a distância correta e o tabuleiro começa a se mover.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(xadrez, (0, 0))
    desenha_cena_com_texto(certa2_2,"As peças deslizam pelo tabuleiro, revelando um compartimento secreto.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(xadrez, (0, 0))
    desenha_cena_com_texto(certa2_3,"Dentro do compartimento, você encontra uma chave brilhante.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(xadrez, (0, 0))

def cena_3():
    tela.fill(PRETO)
    tela.blit(xadrez, (0, 0))
    desenha_cena_com_texto(cena3_1, "Quando você entra na sala, você vê um tabuleiro de xadrez gigante.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(xadrez, (0, 0))
    desenha_cena_com_texto(cena3_2,"Mais à frente, você observa que há algo escrito no rodapé do tabuleiro.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(xadrez, (0, 0))
    desenha_cena_com_texto(cena3_3,"Lá tem uma gravura pedinda pra você calcular a distância entre duas peças no tabuleiro e um local para inserir um número.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(xadrez, (0, 0))

def cena_4():
    tela.fill(PRETO)
    tela.blit(cena3, (0, 0))
    desenha_cena_com_texto(cena4_1,"Ao entrar na próxima sala, você sente o ar ficar denso.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(cena3, (0, 0))
    desenha_cena_com_texto2(cena4_2,C4,"No centro, uma figura sombria surge... é o capeta novamente, com um sorriso malicioso no rosto.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(cena3, (0, 0))

    # Capeta falando
    desenha_cena_com_texto2(cena4_3,C5,"Capeta: 'Ora, ora, quem diria que chegaria tão longe. Este é o último desafio! Vamos ver se você é tão inteligente quanto pensa.'")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(cena3, (0, 0))

    desenha_cena_com_texto2(cena4_4,C6,"A sala se ilumina, revelando uma mesa com várias figuras .")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(cena3, (0, 0))
    desenha_cena_com_texto2(cena4_5,C7,"Há um rei, uma rainha, um cavaleiro, um servo e um bobo da corte. Cada um está posicionado em frente a um cenário detalhado de uma mansão.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(cena3, (0, 0))
    desenha_cena_com_texto2(cena4_6,C8,"Capeta: 'Um deles é o culpado de um crime horrendo, e cabe a você descobrir quem é o verdadeiro suspeito.'")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(cena3, (0, 0))

    # Capeta finalizando
    desenha_cena_com_texto2(cena4_7,C9,"Capeta: 'Descubra o assassino ou sofra as consequências. Você só tem uma chance. Faça a escolha certa ou... bem, você já sabe o que acontece.''")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(cena3, (0, 0))

# Função para a cena de resposta errada 1
def cena_resposta_errada_1():
    tela.fill(PRETO)
    desenha_cena_com_texto(errada1_1,"Infelizmente, essa é a resposta errada. O demônio começa a rir histericamente enquanto o chão se transforma em areia movediça.")
    esperar_interacao()
    tela.fill(PRETO)
    desenha_cena_com_texto(errada1_2,"Num piscar de olhos, você começa a afundar lentamente.")
    esperar_interacao()
    tela.fill(PRETO)
    desenha_cena_com_texto(C3,"Demonio: 'Parece que os números não estavam ao seu favor. Que pena... para você!'")
    esperar_interacao()
    tela.fill(PRETO)
    desenha_cena_com_texto(errada1_4,"Você morre afundando, sufocado pelos números.")
    esperar_interacao()
    tela.fill(PRETO)
def final_errado_2():
    tela.fill(PRETO)
    
    # Descrição inicial do erro e o som sinistro

    # O chão desaparece
    desenha_cena_com_texto(errada1_1,"O chão sob o tabuleiro começa a tremer e a desaparecer, revelando um abismo sem fim.")
    esperar_interacao()
    tela.fill(PRETO)
    # Capeta falando e rindo
    desenha_cena_com_texto(C2,"Capeta (rindo de forma macabra): 'Ah, que pena. O xadrez é um jogo de estratégia... e você falhou.'")
    esperar_interacao()
    tela.fill(PRETO)
    # As peças ganham vida e o protagonista cai
    desenha_cena_com_texto(errada1_2,"Antes que você possa reagir, as peças de xadrez ganham vida. O cavalo se lança sobre você, derrubando-o no buraco que se abriu.")
    esperar_interacao()
    tela.fill(PRETO)
    # Desfecho sombrio e a risada do capeta
    desenha_cena_com_texto(errada1_4,"A última coisa que você ouve é a risada triunfante do capeta enquanto tudo se apaga na escuridão do abismo.")
    esperar_interacao()
    tela.fill(PRETO)




# Função para a cena de resposta errada 3
def final_ruim_suspeito():
    tela.fill(PRETO)
    
    # Descrição do erro e o início da consequência
    desenha_cena_com_texto(errada3_1,"O protagonista hesita, mas faz sua escolha, apontando para o suspeito errado.")
    esperar_interacao()
    tela.fill(PRETO)
    desenha_cena_com_texto(errada3_2,"Num instante, as sombras da sala se movem, engolindo-o.")
    esperar_interacao()
    tela.fill(PRETO)
    # Sentindo a escuridão e a gargalhada do capeta
    desenha_cena_com_texto(errada3_3,"Ele sente a escuridão apertar ao seu redor, sufocante e fria. O capeta gargalha, triunfante.")
    esperar_interacao()
    tela.fill(PRETO)
    # Capeta falando
    desenha_cena_com_texto(C4,"Capeta: 'Você errou... e agora pertence a mim!'")
    esperar_interacao()
    tela.fill(PRETO)
    # Desfecho trágico
    desenha_cena_com_texto(errada3_5,"As sombras o arrastam para o chão, e o protagonista é consumido pela escuridão. Sua última visão é o sorriso cruel do capeta.")
    esperar_interacao()
    tela.fill(PRETO)
def final_feliz_suspeito():
    tela.fill(PRETO)
    tela.blit(cena3, (0, 0))
    # Descrição da escolha certa e a reação do capeta
    desenha_cena_com_texto(errada3_1,"Com um último suspiro, o protagonista aponta para o verdadeiro culpado.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(cena3, (0, 0))
    desenha_cena_com_texto(certa3_2,"O capeta se retrai, seu rosto se contorce em fúria.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(cena3, (0, 0))
    
    # Capeta falando
    desenha_cena_com_texto(certa3_3,"Capeta: 'Você me venceu... desta vez.'")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(cena3, (0, 0))
    
    # Capeta desaparece e a sala se transforma
    desenha_cena_com_texto(certa3_4,"Em uma nuvem de fumaça, o capeta desaparece, e a sala se transforma.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(cena3, (0, 0))
    
    # Descrição do final feliz com a porta dourada
    desenha_cena_com_texto(certa3_5,"Uma porta dourada surge e, ao atravessá-la, o protagonista sente o calor do sol e o frescor do ar.")
    esperar_interacao()
    tela.fill(PRETO)
    tela.blit(fundo1, (0, 0))

    


# Configurações da tela

def tela_vitoria():
    """Função para exibir uma tela de vitória com texto, imagens e símbolos matemáticos."""
    # Fontes para os textos
    fonte_grande = pygame.font.Font(pygame.font.match_font('arial'), 80)  # Fonte "Arial" ou similar
    fonte_media = pygame.font.Font(None, 50)
    texto_vitoria = pygame.font.SysFont("niagarasolid", 150)  # Fonte Niagara Solid, tamanho 80
    fonte_instrucoes = pygame.font.SysFont("chiller", 45)  
    # Cores
    verde = (0, 255, 0)
    sombra = (0, 100, 0)
    branco = (255, 255, 255)
    amarelo_ouro = (255, 215, 0)
    simbolos = ["+", "-", "*", "/", "=", "%", "∫", "√","π", "∞", "∂", "∫", "≈", "≠", "≤", "≥","<",">"]

    for i, simbolo in enumerate(simbolos):

        texto_simbolo = fonte_instrucoes.render(simbolo, True, CINZA )
        
        # Define uma posição aleatória para o símbolo na tela
        x = 150 + (i * 140) % 500
        y = 50 + (i *  50) % 500


        tela.blit(texto_simbolo, (x, y))


    # Renderiza o texto "Vitória" com sombra
    texto_vitoria_sombra = texto_vitoria.render("Vitória", True, sombra)
    texto_vitoria = texto_vitoria.render("Vitória", True, verde)

    # Renderiza o texto "Obrigado por ter jogado!"
    texto_obrigado = fonte_media.render("Obrigado por ter jogado!", True, branco)
    
    # Posições dos textos
    texto_vitoria_rect = texto_vitoria.get_rect(center=(400, 150))
    texto_obrigado_rect = texto_obrigado.get_rect(center=(400, 250))
    
    # Renderiza o texto "Vitória" com sombra e depois o texto em verde por cima
    tela.blit(texto_vitoria_sombra, (texto_vitoria_rect.x + 4, texto_vitoria_rect.y + 4))  # Sombra com deslocamento
    tela.blit(texto_vitoria, texto_vitoria_rect)  # Texto principal em verde

    # Renderiza o texto "Obrigado por ter jogado!"
    tela.blit(texto_obrigado, texto_obrigado_rect)

    # Posiciona e renderiza as imagens
    tela.blit(cena1_1, (-250, 0))
    # Posiciona e renderiza as imagens
    tela.blit(C1, (450, 0))
    # Exibe símbolos matemáticos ao redor da tela

    pygame.display.flip()  # Atualiza a tela

    # Aguarda a interação do jogador
    esperando_interacao = True
    esperando = True
    while esperando:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_r:
                            return reiniciar_jogo()
                        elif evento.key == pygame.K_ESCAPE:
                          
                            sys.exit()

    # Chama a função da tela de vitória
   

def tela_game_over():
    tela.fill(PRETO)  # Preenche a tela com a cor preta

    # Usando a fonte "Courier New" para um estilo mais retrô
    fonte_game_over = pygame.font.SysFont("niagarasolid", 150)  # Fonte Niagara Solid, tamanho 80
    fonte_instrucoes = pygame.font.SysFont("chiller", 25)    # Fonte Chiller, tamanho 25

    # Obtém as dimensões da tela diretamente
    largura = tela.get_width()
    altura = tela.get_height()

    # Texto de "Game Over" com efeito de sombra
    texto_game_over = fonte_game_over.render("GAME OVER", True, (255, 0, 0))  # Texto vermelho
    sombra_game_over = fonte_game_over.render("GAME OVER", True, (100, 0, 0))  # Sombra escura
    texto_rect_game_over = texto_game_over.get_rect(center=(largura // 2, altura // 2 - 100))  # Centraliza no meio
    sombra_rect_game_over = sombra_game_over.get_rect(center=(largura // 2 + 5, altura // 2 - 95))  # Sombra deslocada levemente

    # Texto para as instruções
    texto_instrucoes = fonte_instrucoes.render("Pressione R para recomeçar", True, (255, 255, 255))  # Instruções em branco
    texto_instrucoes2 = fonte_instrucoes.render("Pressione ESC para sair", True, (255, 255, 255))  # Outra linha de instrução
    texto_rect_instrucoes = texto_instrucoes.get_rect(center=(largura // 2, altura // 2 + 50))  # Posiciona abaixo do "Game Over"
    texto_rect_instrucoes2 = texto_instrucoes2.get_rect(center=(largura // 2, altura // 2 + 100))  # Segunda linha das instruções

    # Desenha a sombra e o texto "Game Over"
    tela.blit(sombra_game_over, sombra_rect_game_over)  # Desenha a sombra primeiro
    tela.blit(texto_game_over, texto_rect_game_over)  # Desenha o texto sobre a sombra

    # Desenha as instruções
    tela.blit(texto_instrucoes, texto_rect_instrucoes)
    tela.blit(texto_instrucoes2, texto_rect_instrucoes2)

    # Adiciona um leve brilho ao redor do "Game Over"
   
    pygame.display.flip()  # Atualiza a tela

    # Aguarda a interação do jogador
    esperando_interacao = True
    esperando = True
    while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        return reiniciar_jogo()
                    elif evento.key == pygame.K_ESCAPE:
                        run_game()
                    
                        


# Função para lidar com desafios matemáticos
# Função para lidar com desafios matemáticos
def desafio_1():
    transparente()
    # Blita a superfície transparente na tela
    
    
    # Blita o fundo2 na tela
    tela.blit(fundo2, (0, 0))
    transparente()
    desenha_texto("Desafio 1: Resolva a seguinte equação matemática:", (30, 50), BRANCO)
    
    desenha_texto("Qual é o valor de x na equação 2x + 5 = 15?", (30, 100), BRANCO)

    # Opções de resposta, incluindo "Fugir da Capeta"
    opcoes = ["x = 5", "x = 10", "x = -5", "Fugir da Capeta"]
    
    # Desenhar as caixas de resposta
    caixas_respostas = []
    caixas_respostas.append(desenha_caixa_resposta(f"a) {opcoes[0]}", 50, 150, 700, 50, BRANCO))
    caixas_respostas.append(desenha_caixa_resposta(f"b) {opcoes[1]}", 50, 200, 700, 50, BRANCO))
    caixas_respostas.append(desenha_caixa_resposta(f"c) {opcoes[2]}", 50, 250, 700, 50, BRANCO))
    caixas_respostas.append(desenha_caixa_resposta(f"d) {opcoes[3]}", 50, 300, 700, 50, BRANCO))

    pygame.display.flip()

    # Resposta correta para o desafio 1
    return "x = 5", caixas_respostas, opcoes



# Função para verificar se o clique do jogador foi em uma das caixas de resposta
def desafio_geometria_analitica():
    transparente()
    tela.blit(xadrez, (0, 0))
    transparente()
    # Peças com suas coordenadas ajustadas no tabuleiro para gerar distâncias inteiras
    pecas = [
        {"nome":"Cavalo(3,2) e Rainha (6,6)","certa": "5"},  # Cavalo (3,2) -> Rainha (6,6) -> distância correta = 5
        {"nome":"Bispo(1,1) e Torre (7,1)","certa": "6"},  # Bispo (1,1) -> Torre (7,1) -> distância correta = 6 (Ajustado para Torre correta)
        {"nome":"Peão(4,4) e Rei (7,4)","certa": "3"},  # Peão (4,4) -> Rei (7,4) -> distância correta = 3
 
        ]

    # Escolher uma junção aleatoriamente
    funcao_escolhida =  random.choice(pecas)

    # Mostrar o desafio na tela com as posições das peças
    texto_pergunta = f"Qual a distância entre {funcao_escolhida['nome']})?"
    desenha_texto(texto_pergunta, (30, 50), BRANCO)

    # Gerar respostas incorretas e garantir que todas sejam inteiros
    respostas = [funcao_escolhida["certa"]]
    while len(respostas) < 4:  # Agora são 4 opções
        resposta_errada = str(random.randint(1, 10))  # Gera respostas incorretas inteiras
        if resposta_errada not in respostas:
            respostas.append(resposta_errada)

    # Salvar a resposta correta antes de embaralhar
  
    random.shuffle(respostas)

    # Embaralhar as respostas
  

    # Identificar a posição correta após o embaralhamento

    # Desenhar as caixas de resposta
    caixas_respostas = []
    caixas_respostas.append(desenha_caixa_resposta(f"1) {respostas[0]}", 50, 300, 700, 50, BRANCO))
    caixas_respostas.append(desenha_caixa_resposta(f"2) {respostas[1]}", 50, 350, 700, 50, BRANCO))
    caixas_respostas.append(desenha_caixa_resposta(f"3) {respostas[2]}", 50, 400, 700, 50, BRANCO))
    caixas_respostas.append(desenha_caixa_resposta(f"4) {respostas[3]}", 50, 450, 700, 50, BRANCO))  # Quarta opção

    pygame.display.flip()

    # Retornar a resposta correta e seu índice após o embaralhamento
    return funcao_escolhida["certa"], caixas_respostas, respostas


# Função para verificar se o clique do jogador foi em uma das caixas de resposta
def verificar_clique(caixas_respostas, resposta_correta, respostas):
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Verificar se o clique foi em uma das caixas de resposta
                for i, caixa in enumerate(caixas_respostas):
                    if caixa.collidepoint(evento.pos):
                        # Caso especial: fuga da Capeta
                        if respostas[i] == "Fugir da Capeta":
                            return "fuga"
                        # Caso resposta correta
                        elif respostas[i] == resposta_correta:
                            return "vitoria"
                        # Caso resposta incorreta
                        else:
                            return "morte"



def desafio_logico():
    tela.blit(cena3, (0, 0))
    transparente()
    desenha_texto("Só uma pessoa diz a verdade, quem é o culpado do crime?", (30, 40), BRANCO)
    
    desenha_texto("Rei: 'O criminoso é o cavaleiro'", (30, 80), BRANCO)
    desenha_texto("Rainha: 'O Servo não é o criminoso'", (30, 120), BRANCO)
    desenha_texto("Servo: 'O bobo da corte é o criminoso'", (30, 160), BRANCO)
    desenha_texto("Cavaleiro: 'Eu não sou o criminoso'", (30, 200), BRANCO)
    desenha_texto("Bobo da corte: 'A rainha está falando a verdade'", (30, 240), BRANCO)

    # Opções de resposta
    opcoes = ["Rei", "Rainha", "Servo", "Cavaleiro","Bobo da corte"]
    
    # Desenhar as caixas de resposta
    caixas_respostas = []
    caixas_respostas.append(desenha_caixa_resposta(f"a) {opcoes[0]}", 50, 300, 700, 50, BRANCO))
    caixas_respostas.append(desenha_caixa_resposta(f"b) {opcoes[1]}", 50, 350, 700, 50, BRANCO))
    caixas_respostas.append(desenha_caixa_resposta(f"c) {opcoes[2]}", 50, 400, 700, 50, BRANCO))
    caixas_respostas.append(desenha_caixa_resposta(f"d) {opcoes[3]}", 50, 450, 700, 50, BRANCO))
    caixas_respostas.append(desenha_caixa_resposta(f"e) {opcoes[4]}", 50, 500, 700, 50, BRANCO))

    pygame.display.flip()

    return "Servo", caixas_respostas, opcoes


# Função para mostrar os diferentes finais
# Função para mostrar os diferentes finais

def mostrar_final(final):
    tela.fill(PRETO)
    
    if final == "vitoria":
        desenha_texto("Parabéns! Você resolveu o enigma e escapou!", (30, 250), VERDE)
    elif final == "morte":
        desenha_texto("Você errou! Pressione 'R' para reiniciar ou 'ESC' para sair.", (30, 250), VERMELHO)
    elif final == "final_bom":
        desenha_texto("Você solucionou o enigma e descobriu a verdade!", (30, 250), VERDE)
    elif final == "final_ruim":
        desenha_texto("Você fez a escolha errada e a verdade escapou!", (30, 250), VERMELHO)
         
    elif final == "fuga":
        # Final "fuga" com rolagem de texto
        textos_fuga = [
            "Correr da Capeta",
            "Ao tentar correr, a Capeta apenas suspira",
            "'Típico... fugir nunca é a solução.'",
            "Com um simples olhar, ela transforma seus pés",
            "em raízes presas ao chão.",
            "Você assiste a Capeta lentamente aproximar-se...",
            "E ela comenta sarcasticamente: 'Nunca quis ser jardineira,",
            "mas talvez seja bom cultivar uns matemáticos por aqui.'",
            "Você é transformado em uma estátua de pedra,",
            "eternamente enraizado naquele lugar."
        ]
        
        y_posicao = altura  # Inicia fora da tela
        y_parada = (altura - len(textos_fuga) * 50) // 2
        velocidade = 2  # Controla a velocidade de subida
        BORDAO = (128, 0, 32)  # Cor para o texto

        interromper_rolagem = False  # Flag para interromper rolagem
        clock = pygame.time.Clock()

        # Flag para exibir a mensagem de reinício após o clique
        exibir_mensagem_reinicio = False

        while y_posicao > y_parada and not interromper_rolagem:
            tela.fill(PRETO)

            # Desenha cada linha do texto
            for i, texto in enumerate(textos_fuga):
                desenha_texto(texto, (30, y_posicao + i * 50), BORDAO)
            
            pygame.display.flip()
            pygame.time.delay(40)
            y_posicao -= velocidade  # Move o texto para cima

            # Checa eventos enquanto o texto rola
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        return "reiniciar"
                    elif evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    
                    pygame.display.flip()

               

    pygame.display.flip()
    
    # Desabilitar interações se o final for "morte" ou "fuga"
    if final in ["morte", "final_ruim" ]:
        # Loop que impede qualquer interação
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        return "reiniciar"
                    elif evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
        pygame.display.flip()
    
     
        # Loop que impede qualquer interação
    if final == "fuga":
        # Exibe o texto final de "Morte" e desabilita qualquer interação
  

        # Espera a reinicialização ou saída
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    tela_game_over()
                    pygame.display.flip()
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        return "reiniciar"
                    elif evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
          
  
    if final in ["vitoria", "final_bom"]:  
    # Espera o jogador pressionar 'R' para reiniciar, 'ESC' para sair ou clicar para continuar
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        return "reiniciar"
                    elif evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    esperando = False
  
    return "continuar"
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Menu Matemático de Terror")

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        
        # Eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        if button["text"] == "Jogar":
                            jogo()
                        elif button["text"] == "Sobre":
                            open_options_screen()
                        elif button["text"] == "Creditos":
                            open_credits_screen(screen)
                        elif button["text"] == "Sair":
                            running = False

        draw_title()
        draw_buttons()
        draw_symbol_circle( WIDTH - 120, 120, radius=200, angle_speed=-0.002, scale=0.8)
        draw_symbol_circle( 80, HEIGHT - 80, radius=200, angle_speed=0.0015, scale=0.8)
        pygame.display.flip()

# Função principal do jogo
def jogo():
    pular_cenas = False

    
    while True:
        # Cena inicial
        if not pular_cenas:
            
            cena_inicial()
            
            cena_2()
           
        # Verificar interações do usuário (isso é muito importante)
     
        # Desafio 1
        resposta_correta, caixas_respostas, respostas = desafio_1()
        escolha = verificar_clique(caixas_respostas, resposta_correta, respostas)

        if escolha == "fuga":
            resultado = "fuga"
        elif escolha == "vitoria":
            resultado = cena_resposta_correta()
            cena_3 ()
            
        else:
            resultado = cena_resposta_errada_1()
            tela_game_over()

        # Mostra o resultado do desafio 1 e verifica se o jogador quer reiniciar
        acao = mostrar_final(resultado)
        if acao == "reiniciar":
            pular_cenas = False
            tela_game_over()
            continue  # Reinicia o jogo voltando à cena inicial

        # Desafio 2: Matemática (um pouco mais avançada)
        resposta_correta, caixas_respostas, respostas = desafio_geometria_analitica()
        escolha = verificar_clique(caixas_respostas, resposta_correta, respostas)

        if escolha == "vitoria":
            resultado = cena_resposta_correta_2()
            cena_4 ()

        else:
            resultado = final_errado_2()
            tela_game_over()

        # Mostra o resultado do desafio 2 e verifica se o jogador quer reiniciar
        acao = mostrar_final(resultado)
        if acao == "reiniciar":
            pular_cenas = False
            continue  # Reinicia o jogo voltando à cena inicial

        # Desafio 3: Lógica dos suspeitos
        resposta_correta, caixas_respostas, respostas = desafio_logico()
        escolha = verificar_clique(caixas_respostas, resposta_correta, respostas)

        if escolha == "vitoria":
            resultado = final_feliz_suspeito()
            
        else:
            resultado = final_ruim_suspeito()
            tela_game_over()
        # Mostra o resultado do desafio 3 e verifica se o jogador quer reiniciar
        acao = mostrar_final(resultado)
        if acao == "reiniciar":
            pular_cenas = False
            continue  # Reinicia o jogo voltando à cena inicial

        # Final de vitória se todos os desafios foram corretos
        tela_vitoria()
        break


# Loop principal do jogo
async def main():
    while True:
        run_game()
        jogo()
        pygame.display.update()
        await asyncio.sleep(0)
asyncio.run(main())