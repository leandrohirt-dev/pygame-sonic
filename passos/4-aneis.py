import pygame
import math

pygame.init()
tela = pygame.display.set_mode((600, 400))
relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 36)
MUNDO = 4000
sonic = pygame.Rect(60, 318, 32, 32)
vel_x = 0
vel_y = 0
lado = 1
giro = 0
no_chao = True
camera = 0
aneis = [pygame.Rect(x + i * 32, 322, 16, 16)
         for x in range(500, 3700, 400)
         for i in range(6)]
contador = 0
ESPINHOS = [(0, -16), (-26, -14), (-10, -6), (-28, 0),
            (-10, 4), (-22, 12), (0, 8)]


def desenha_sonic(cx, cy):
    espinhos = [(cx + lado * x, cy + y)
                for x, y in ESPINHOS]
    pygame.draw.polygon(tela, "#1E5BD8", espinhos)
    pygame.draw.circle(tela, "#1E5BD8", (cx, cy - 3), 14)
    pygame.draw.circle(tela, "#F2C79A",
                       (cx + lado * 7, cy + 3), 7)
    olho = (cx + lado * 6 - 5, cy - 13, 10, 13)
    pygame.draw.ellipse(tela, "white", olho)
    pygame.draw.circle(tela, "black",
                       (cx + lado * 8, cy - 6), 2)
    pygame.draw.ellipse(tela, "#E53935",
                        (cx - 15, cy + 9, 15, 7))
    pygame.draw.ellipse(tela, "#E53935",
                        (cx, cy + 9, 15, 7))


def desenha_bola(cx, cy):
    pygame.draw.circle(tela, "#1E5BD8", (cx, cy), 16)
    for k in range(3):
        a = giro + k * 2.1
        ponta = (cx + 15 * math.cos(a),
                 cy + 15 * math.sin(a))
        pygame.draw.line(tela, "#123C99", (cx, cy),
                         ponta, 4)


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and no_chao:
                vel_y = -12
                no_chao = False

    teclas = pygame.key.get_pressed()
    direcao = (teclas[pygame.K_RIGHT]
               - teclas[pygame.K_LEFT])
    if direcao:
        vel_x += 0.2 * direcao
        lado = direcao
    else:
        vel_x *= 0.95
    vel_x = max(-12, min(12, vel_x))
    sonic.x += round(vel_x)
    sonic.x = max(0, min(MUNDO - 32, sonic.x))

    vel_y += 0.6
    sonic.y += round(vel_y)
    if sonic.bottom >= 350:
        sonic.bottom = 350
        vel_y = 0
        no_chao = True
    giro += 0.4 * lado

    for anel in aneis[:]:
        if sonic.colliderect(anel):
            aneis.remove(anel)
            contador += 1

    camera = max(0, min(sonic.centerx - 250,
                        MUNDO - 600))
    tela.fill("#5AB0F5")
    fundo = camera // 4 % 300
    for x in range(-300, 900, 300):
        pygame.draw.ellipse(tela, "#2E9E4A",
                            (x - fundo, 230, 340, 240))
    for x in range(300, MUNDO, 450):
        flor = x - camera
        topo = (flor, 296)
        pygame.draw.line(tela, "#1B6B2A", (flor, 345),
                         topo, 4)
        pygame.draw.circle(tela, "#F7E03C", topo, 11)
        pygame.draw.circle(tela, "#8A4418", topo, 5)
    base = camera // 25
    for i in range(26):
        for j in range(2):
            x = i * 25 - camera % 25
            cor = "#C8702E"
            if (base + i + j) % 2:
                cor = "#8A4418"
            pygame.draw.rect(tela, cor,
                             (x, 355 + j * 25, 25, 25))
    pygame.draw.rect(tela, "#3DBB3D", (0, 345, 600, 12))

    for anel in aneis:
        centro = (anel.centerx - camera, anel.centery)
        pygame.draw.circle(tela, "#FFD23F", centro, 8, 3)

    cx = sonic.centerx - camera
    if no_chao:
        desenha_sonic(cx, sonic.centery)
    else:
        desenha_bola(cx, sonic.centery)

    placar = fonte.render(f"ANÉIS {contador}",
                          True, "white")
    tela.blit(placar, (16, 15))
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
