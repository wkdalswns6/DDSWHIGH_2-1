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

xspeed = 1.08
yspeed = 0.72

xa = -0.00108 / 2
ya = -0.00072 / 2

running = True
while running:
    screen.fill((102, 102, 102))  # 색상 설정

    # 종료 조건 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 등가속 => 일정한 가속도만큼 속도가 바뀜
    xspeed += xa
    yspeed += ya

    # 브레이크
    # if xspeed < 0:
    #     xspeed = 0
    # if yspeed < 0:
    #     yspeed = 0

    # 등속 => 일정한 속도만큼 위치가 바뀜
    xpos += xspeed
    ypos += yspeed

    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), rad)

    # 화면 업데이트
    pygame.display.update()
