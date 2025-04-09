import pygame

def play(filename):
    pygame.mixer.init(frequency=16000)  # Initsialiseerib Pygame'i helimooduli
    pygame.mixer.music.load(filename)   # Laeb muusika faili
    pygame.mixer.music.play(-1)          # Mängib muusikat lõpmatult (kordub lõputult)

# Mängu algus
pygame.init()

# Mängu akna seadistamine
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mängu Pealkiri")

# Taustamuusika mängimine
play("Muusika.mp3")  # Laadib ja mängib taustamuusika

import pygame  # Impordime Pygame'i

# Initsialiseerime Pygame'i
pygame.init()

# Määrame ekraani suuruse ja loome akna
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pall ja Alus")

# Värvid RGB formaadis
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (211, 211, 211)  # Heledam hallikas taust

# Laeme pildid (peavad olema samas kaustas)
ball_image = pygame.image.load('ball.png')       # Palli pilt
paddle_image = pygame.image.load('pad.png')      # Aluse (paddle) pilt

# Palli suurus ja liikumiskiirus
BALL_SIZE = 20
ball_speed_x = 4   # Kiirus horisontaalsuunas
ball_speed_y = 4   # Kiirus vertikaalsuunas

# Aluse suurus ja kiirus
PADDLE_WIDTH = 120
PADDLE_HEIGHT = 20
PADDLE_SPEED = 6   # Kiirus, millega alus liigub

# Algpositsioonid pallile
ball_rect = ball_image.get_rect()
ball_rect.x = (WIDTH - BALL_SIZE) // 2
ball_rect.y = (HEIGHT - BALL_SIZE) // 2

# Algpositsioon alusele (ekraani keskelt allpool)
paddle_rect = paddle_image.get_rect()
paddle_rect.x = (WIDTH - PADDLE_WIDTH) // 2
paddle_rect.y = int(HEIGHT / 1.5)

# Skoor ja fonti seadistus
score = 0
font = pygame.font.Font(None, 36)

# Mängu tsükkel algab
running = True
while running:
    screen.fill(LIGHT_GRAY)  # Taustavärv igal kaadril

    # Kontrollime sündmusi (nt akna sulgemine)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Klahvide lugemine aluse liikumiseks
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_rect.x -= PADDLE_SPEED  # Liigu vasakule
    if keys[pygame.K_RIGHT]:
        paddle_rect.x += PADDLE_SPEED  # Liigu paremale

    # Takistame alusel ekraanilt välja liikumast
    if paddle_rect.left < 0:
        paddle_rect.left = 0
    if paddle_rect.right > WIDTH:
        paddle_rect.right = WIDTH

    # Palli liikumine
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # Põrkumine vasaku ja parema servaga
    if ball_rect.left <= 0 or ball_rect.right >= WIDTH:
        ball_speed_x *= -1

    # Põrkumine ülemise servaga
    if ball_rect.top <= 0:
        ball_speed_y *= -1

    # Kui pall puudutab alumist serva → mäng lõppeb
    if ball_rect.bottom >= HEIGHT:
        running = False

    # Kui pall puutub alust ja liigub alla → põrkab
    if ball_rect.colliderect(paddle_rect) and ball_speed_y > 0:
        ball_speed_y *= -1
        score += 1  # Lisame punkti

    # Joonistame palli ja aluse
    screen.blit(ball_image, ball_rect)
    screen.blit(paddle_image, paddle_rect)

    # Kuvame skoori ekraani vasakus ülanurgas
    score_text = font.render(f"Skoor: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Värskendame ekraani
    pygame.display.flip()

    # Seame kaadrisageduse (~60 fps)
    pygame.time.Clock().tick(60)

# Kui mäng lõppeb
pygame.quit()

