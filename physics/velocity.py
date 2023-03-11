import pygame

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
clock.tick(60)

xpos = 0
ypos = 0
rad = 20

xspeed = 0.108
yspeed = 0.072

running = True
while running:
    screen.fill((102, 102, 102))  # 색상 설정

    # 종료 조건 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    xpos += xspeed
    ypos += yspeed
    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), rad)

    # 화면 업데이트
    pygame.display.update()
