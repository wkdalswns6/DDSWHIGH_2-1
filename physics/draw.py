import pygame

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 340

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
clock.tick(60)

running = True
while running:
    screen.fill((255, 255, 0))  # 색상 설정

    # 종료 조건 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
