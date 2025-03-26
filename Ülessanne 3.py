import pygame
import sys

# Initsialiseerib pygame
pygame.init()

# Ekraani seaded
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Ruudud ekraanil")

# Värvid
lGreen = [153, 255, 153]  # Taustavärv (roheline)
red = [255, 0, 0]  # Punane värv (ruudud)

# Ekraan täidetakse algselt rohelise värviga
screen.fill(lGreen)

# Funktsioon, mis joonistab ruudud
def draw_grid(square_size, rows, cols, line_color):
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(screen, line_color, [col * square_size, row * square_size, square_size, square_size], 1)

# Mängu tsükkel
gameover = False

while not gameover:
    # Loob ruudud ekraanil
    draw_grid(20, 24, 32, red)  # Ruudud suurusega 20px, 24 rida ja 32 veergu, joone värv punane

    # Ekraanil olevate objektide kuvamine
    pygame.display.flip()

    # Sündmuste käsitlemine (sulgemine ristist)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True  # Kui on sulgemise sündmus, lõpetame mängu tsükli

# Lõpetab pygame'i, kui tsükkel on lõppenud
pygame.quit()
sys.exit()
