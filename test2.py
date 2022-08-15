import pygame
pygame.init()

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
			
rect1 = pygame.Rect((0, 0), (32, 32))
rect2 = pygame.Rect((0, 0), (32, 32))
image = pygame.Surface((32, 32))
image.fill(WHITE)

forward1 = True
forward2 = True

while True:
  clock.tick(FPS)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

  if forward1:
    rect1.move_ip(6, 0)
  else:
    rect1.move_ip(-6, 0)

  if forward2:
    rect2.move_ip(0, 6)
  else:
    rect2.move_ip(0, -6)

  if rect1.x > 720 - rect1.w:
    forward1 = False
  elif rect1.x < 0:
    forward1 = True

  if rect2.y > 480 - rect2.h:
    forward2 = False
  elif rect2.y < 0:
    forward2 = True

  screen.fill(BLACK)
  screen.blit(image, rect1)
  screen.blit(image, rect2)
  pygame.display.update()
