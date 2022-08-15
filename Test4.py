# Represent each space ship as a table

import pygame
pygame.init()

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

spaceShip1 = {
  "rect"    : pygame.Rect((0, 0), (32, 32)),
  "image"   : pygame.Surface((32, 32)),
  "forward" : True,
  "speed"   : 18
}

spaceShip2 = {
  "rect"    : pygame.Rect((0, 34), (32, 32)),
  "image"   : pygame.Surface((32, 32)),
  "forward" : True,
  "speed"   : 9
}

spaceShip1["image"].fill(WHITE)
spaceShip2["image"].fill(RED)

while True:
  clock.tick(FPS)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

  if spaceShip1["forward"]:
    spaceShip1["rect"].move_ip(spaceShip1["speed"], 0)
  else:
    spaceShip1["rect"].move_ip(-spaceShip1["speed"], 0)

  if spaceShip2["forward"]:
    spaceShip2["rect"].move_ip(spaceShip2["speed"], 0)
  else:
    spaceShip2["rect"].move_ip(-spaceShip2["speed"], 0)

  if spaceShip1["rect"].x > 720 - spaceShip1["rect"].w:
    spaceShip1["forward"] = False
  elif spaceShip1["rect"].x < 0:
    spaceShip1["forward"] = True

  if spaceShip2["rect"].x > 720 - spaceShip2["rect"].h:
    spaceShip2["forward"] = False
  elif spaceShip2["rect"].x < 0:
    spaceShip2["forward"] = True

  screen.fill(BLACK)
  screen.blit(spaceShip1["image"], spaceShip1["rect"])
  screen.blit(spaceShip2["image"], spaceShip2["rect"])
  pygame.display.update()
