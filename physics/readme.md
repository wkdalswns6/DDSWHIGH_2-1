# 물리 효과 구현 프로젝트

## draw.py

> pygame 모듈을 사용하여 화면을 그리기

### ✨ pygame 설치

```
python3 -m pip install pygame
```

### ✨ pygame 모듈 불러오기

```python
import pygame
```

### ✨ pygame 초기화

```python
pygame.init()
```

### ✨ pygame 해상도 정하기

```python
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 340

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
```

### ✨ pygame 프레임 정하기

```python
clock = pygame.time.Clock()
clock.tick(60) #60프레임으로 설정
```

### ✨ pygame 화면 구성

```python
running = True
while running:
    screen.fill((255, 255, 0))  # 색상 설정

    # 종료 조건 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 업데이트
    pygame.display.update()
```

---

## draw_circle.py

> 원 그리기

### ✨ pygame 원 그리기

```python
#좌표,반지름은 변칙적임으로 변수 설정
 pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), rad)
```

---

## velocity.py

> 원 움직이기

### ✨ pygame 원 이동하기

```python
#같은 방향으로 1프레임당 xspeed 만큼 더한다(등속운동)
#같은 방향으로 1프레임당 yspeed 만큼 더한다.
xpos += xspeed
ypos += yspeed
pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), rad)
```

---

## accel.py

```python
# 같은 가속도 만큼 더해준다.(등가속도운동)
xspeed += xa # xa = 가속도
yspeed += ya # ya = 가속도
```
