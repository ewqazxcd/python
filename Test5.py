# Avoid repetition by using a function

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

def move_ship(ship):
  if ship["forward"]:
    ship["rect"].move_ip(ship["speed"], 0)
  else:
    ship["rect"].move_ip(-ship["speed"], 0)

def bounce_ship(ship):
  if ship["rect"].x > 720 - ship["rect"].w:
    ship["forward"] = False
  elif ship["rect"].x < 0:
    ship["forw      ard"] = True

while True:
  clock.tick(FPS)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

  move_ship(spaceShip1)
  move_ship(spaceShip2) 
  
  bounce_ship(spaceShip1)
  bounce_ship(spaceShip2)
  
  screen.fill(BLACK)
  screen.blit(spaceShip1["image"], spaceShip1["rect"])
  screen.blit(spaceShip2["image"], spaceShip2["rect"])
  pygame.display.update()
