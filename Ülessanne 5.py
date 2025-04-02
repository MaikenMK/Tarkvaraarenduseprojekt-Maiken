import pygame

# Pygame initsialiseerimine
pygame.init()

# Ekraani suurus ja seadistamine
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pall ja Alus")

# Värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (211, 211, 211)  # Heledam taustavärv

# Laeme pildid
ball_image = pygame.image.load('ball.png')  # Laeb palli pildi
paddle_image = pygame.image.load('pad.png')  # Laeb aluse pildi

# Palli suurus ja liikumiskiirus
BALL_SIZE = 20
ball_speed_x = 4
ball_speed_y = 4

# Aluse suurus ja kiirus
PADDLE_WIDTH = 120
PADDLE_HEIGHT = 20
PADDLE_SPEED = 4

# Algseaded
ball_rect = ball_image.get_rect()
ball_rect.x = (WIDTH - BALL_SIZE) // 2
ball_rect.y = (HEIGHT - BALL_SIZE) // 2

paddle_rect = paddle_image.get_rect()
paddle_rect.x = (WIDTH - PADDLE_WIDTH) // 2
paddle_rect.y = HEIGHT // 1.5  # Alus on keskkohast allpool

# Skoor
score = 0
font = pygame.font.Font(None, 36)

# Aluse liikumine
paddle_direction = 1  # 1 - liikumine paremale, -1 - liikumine vasakule

# Mängu tsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Palli liikumine
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # Palli põrkamine seintelt
    if ball_rect.left <= 0 or ball_rect.right >= WIDTH:
        ball_speed_x *= -1  # Põrkab vasakult või paremalt seinalt
    if ball_rect.top <= 0:
        ball_speed_y *= -1  # Põrkab ülemisest servast
    if ball_rect.bottom >= HEIGHT:
        ball_speed_y *= -1  # Põrkab alumisest servast

    # Kokkupõrge alusega
    if ball_rect.colliderect(paddle_rect) and ball_speed_y > 0:
        ball_speed_y *= -1  # Kui pall puutub alusega, muudab suunda

        # Kui pall puutub alusega, saab mängija punkti
        score += 1

    # Aluse liikumine
    paddle_rect.x += PADDLE_SPEED * paddle_direction  # Alus liigub

    # Kui alus puudutab ekraani serva, vahetab suunda
    if paddle_rect.left <= 0 or paddle_rect.right >= WIDTH:
        paddle_direction *= -1  # Muudab suunda

    # Joonistame kõik elemendid ekraanile
    screen.fill(LIGHT_GRAY)  # Taustavärv on helehall
    screen.blit(ball_image, ball_rect)  # Pall
    screen.blit(paddle_image, paddle_rect)  # Alus

    # Kuvame skoori
    score_text = font.render(f"Skoor: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()  # Värskendame ekraani

    pygame.time.Clock().tick(60)  # Reguleerime mängu kiirus

# Lõpetame Pygame
pygame.quit()
