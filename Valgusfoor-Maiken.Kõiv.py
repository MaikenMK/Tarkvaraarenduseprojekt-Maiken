import pygame

pygame.init()

# Ekraani loomine
screen = pygame.display.set_mode([300, 300])
pygame.display.set_caption("Maikeni Valgusfoor")

# Värvid
punane = (255, 0, 0)
roheline = (0, 255, 0)
kollane = (255, 255, 0)
hall = (150, 150, 150)
must = (0, 0, 0)

# Tausta täitmine mustaks
screen.fill(must)

# Akna keskpunkt
window_center_x = 150
window_center_y = 150

# Ringide raadius (muudetav)
ringi_raadius = 40

# Ringide positsioonid
small_circle_pos = (window_center_x, window_center_y - 85)  # Ülemine ring
medium_circle_pos = (window_center_x, window_center_y)  # Keskmine ring
large_circle_pos = (window_center_x, window_center_y + 85)  # Alumine ring

# Kitsam hallikas ristkülik (joon, mitte täidetud)
rect_width = 90
rect_height = 270
rect_x = window_center_x - rect_width // 2
rect_y = window_center_y - rect_height // 2
pygame.draw.rect(screen, hall, [rect_x, rect_y, rect_width, rect_height], 2)

# Joonista ringid
pygame.draw.circle(screen, punane, small_circle_pos, ringi_raadius)  # Ülemine ring (punane)
pygame.draw.circle(screen, kollane, medium_circle_pos, ringi_raadius)  # Keskmine ring (kollane)
pygame.draw.circle(screen, roheline, large_circle_pos, ringi_raadius)  # Alumine ring (roheline)

# Ekraani uuendamine
pygame.display.flip()

# Pygame loop, et aken ei sulguks kohe
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
