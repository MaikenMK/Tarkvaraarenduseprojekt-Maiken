import pygame
import random

# Pygame initsialiseerimine
pygame.init()

# Ekraani seaded
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ringide Mäng")

# Värvid
LIGHT_BLUE = (173, 216, 230)  # Taustavärv
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]  # Võimalikud ringi värvid

# Ringide andmestruktuur (positsioon, suurus, värv, liikumissuund)
circles = []
MAX_CIRCLES = 10
SPEED = 2  # Ringide liikumise kiirus

running = True
while running:
    screen.fill(LIGHT_BLUE)  # Tausta värvimine

    # Sündmuste käsitlemine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Hiireklikiga lisame uue ringi
            if len(circles) >= MAX_CIRCLES:
                circles.pop(0)  # Kustutame esimese ringi, kui limiit on täis
            x, y = event.pos
            size = 10  # Algne suurus
            color = random.choice(colors)  # Juhuslik värv
            dx, dy = random.choice([-SPEED, SPEED]), random.choice([-SPEED, SPEED])  # Juhuslik suund
            circles.append([x, y, size, color, dx, dy])  # Lisame ringi listi

    # Ringide liikumine ja joonistamine
    for circle in circles:
        circle[0] += circle[4]  # Muudame x-koordinaati
        circle[1] += circle[5]  # Muudame y-koordinaati

        # Servadelt põrkumine
        if circle[0] - circle[2] <= 0 or circle[0] + circle[2] >= WIDTH:
            circle[4] *= -1  # Muudame x-suunalist liikumist
        if circle[1] - circle[2] <= 0 or circle[1] + circle[2] >= HEIGHT:
            circle[5] *= -1  # Muudame y-suunalist liikumist

        # Suurendame ringi iga tsükliga
        circle[2] += 0.2  # Ring kasvab ajaga
        pygame.draw.circle(screen, circle[3], (int(circle[0]), int(circle[1])), int(circle[2]))

    pygame.display.flip()  # Kuvame uuendatud ekraani
    pygame.time.delay(30)  # Väike paus, et animatsioon sujuks

pygame.quit()
