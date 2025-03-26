import pygame

# Impordib mooduli ja initsialiseerib pygame
pygame.init()

# Kuvab akna koos resolutsiooniga
aken = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Ülesanne 2")

# Laeb taustapildi
taust = pygame.image.load("bg_shop.png")

# Laeb karakteri ja muudab selle suurust
karakter = pygame.image.load("seller.png")
karakter = pygame.transform.scale(karakter, (255, 305))

# Laeb jutumulli ja muudab selle suurust
mull = pygame.image.load("chat.png")
mull = pygame.transform.scale(mull, (255, 200))

# Muudab teksti fonti ja suurust
font = pygame.font.Font(None, 22)
jutt = font.render("Tere, olen Maiken!", True, [255, 255, 255])

# Mängu tsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kuvab pildid ja teksti
    aken.blit(taust, [0, 0])
    aken.blit(karakter, [105, 160])
    aken.blit(mull, [247, 67])
    aken.blit(jutt, [325, 145])

    pygame.display.flip()

pygame.quit()

