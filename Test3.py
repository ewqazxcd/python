# Two independent space ships

import pygame
pygame.init()

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

rect1 = pygame.Rect((0, 0), (32, 32))
rect2 = pygame.Rect((0, 34), (32, 32))
image1 = pygame.Surface((32, 32))
image2 = pygame.Surface((32, 32))
image1.fill(WHITE)
image2.fill(RED)

forward1 = True
forward2 = True

speed1 = 18
speed2 = 9

while True:
  clock.tick(FPS)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

  if forward1:
    rect1.move_ip(speed1, 0)
  else:
    rect1.move_ip(-speed1, 0)

  if forward2:
    rect2.move_ip(speed2, 0)
  else:
    rect2.move_ip(-speed2, 0)

  if rect1.x > 720 - rect1.w:
    forward1 = False
  elif rect1.x < 0:
    forward1 = True

  if rect2.x > 720 - rect2.h:
    forward2 = False
  elif rect2.x < 0:
    forward2 = True

  screen.fill(BLACK)
  screen.blit(image1, rect1)
  screen.blit(image2, rect2)
  pygame.display.update()
