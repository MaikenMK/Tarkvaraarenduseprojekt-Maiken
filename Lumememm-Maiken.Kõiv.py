import pygame
pygame.init()
screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Maikeni Lumememm")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
small_circle_radius = 32  # Väike ring (ülemine)
medium_circle_radius = 42  # Keskmine ring
large_circle_radius = 50  # Suur ring (alumine)

# Ringide asukohad
small_circle_pos = (20, 20)  # Ülemine ring
medium_circle_pos = (150, 60)  # Keskmine ring
large_circle_pos = (160, 100)  # Alumine ring
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Täidab ekraani valgega
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, small_circle_pos, small_circle_radius)
    pygame.draw.circle(screen, WHITE, medium_circle_pos, medium_circle_radius)
    pygame.draw.circle(screen, WHITE, large_circle_pos, large_circle_radius)

    window_center_x = 150
    window_center_y = 150
    small_circle_pos = (window_center_x, window_center_y - 70)  # Ülemine ring
    medium_circle_pos = (window_center_x, window_center_y)  # Keskmine ring
    large_circle_pos = (window_center_x, window_center_y + 80)  # Alumine ring
    pygame.draw.polygon(screen, (255, 0, 0), [(145, 83), (155, 83), (150, 99)])

    pygame.draw.circle(screen, BLACK, (162, 70), 4)  # Vasak silm
    pygame.draw.circle(screen, BLACK, (140, 70), 4)  # Parem silm


    # Ekraani uuendamine
    pygame.display.flip()