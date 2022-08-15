  # e

import pygame
pygame.init()

screen = pygame.display.set_mode((704, 480))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

rect1 = pygame.Rect((0, 0), (32, 32))
image1 = pygame.Surface((32, 32))
image1.fill(WHITE)

while True:
  clock.tick(FPS)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        if rect1.x > 0:
          rect1.move_ip (-32, 0)
      elif event.key == pygame.K_RIGHT:
        if rect1.x < 672:
          rect1.move_ip (32, 0)
      elif event.key == pygame.K_UP:
        if rect1.y > 0:
          rect1.move_ip (0, -32)
      elif event.key == pygame.K_DOWN:
        if rect1.y < 440 :
          rect1.move_ip (0, 32)
      elif event.key == pygame.K_Q  :
        quit()

  screen.fill(BLACK)
  screen.blit(image1, rect1)
  pygame.display.update()
