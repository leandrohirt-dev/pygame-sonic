import pygame

pygame.init()
tela = pygame.display.set_mode((600, 400))
relogio = pygame.time.Clock()
MUNDO = 4000
sonic = pygame.Rect(60, 318, 32, 32)
lado = 1
camera = 0
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


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

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

    cx = sonic.centerx - camera
    desenha_sonic(cx, sonic.centery)
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
