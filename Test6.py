# Introduce many space ships, and use images instead of squares

import pygame
pygame.init()

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)

all_ships = [
  { "rect"    : pygame.Rect((0, 0), (32, 32)),
    "image"   : pygame.Surface((32, 32)),
    "forward" : True,
    "speed"   : 10
  },
  { "rect"    : pygame.Rect((0, 34), (32, 32)),
    "image"   : pygame.Surface((32, 32)),
    "forward" : True,
    "speed"   : 9
  },
  { "rect"    : pygame.Rect((0, 68), (32, 32)),
    "image"   : pygame.Surface((32, 32)),
    "forward" : True,
    "speed"   : 11
  },
  { "rect"    : pygame.Rect((0, 102), (32, 32)),
    "image"   : pygame.Surface((32, 32)),
    "forward" : True,
    "speed"   : 5
  },
  { "rect"    : pygame.Rect((0, 136), (32, 32)),
    "image"   : pygame.Surface((32, 32)),
    "forward" : True,
    "speed"   : 2
  }
]

i = pygame.image.load("space_ship.png")
all_ships[0]["image"].blit(i, (0,0))
all_ships[1]["image"].blit(i, (0,0))
all_ships[2]["image"].blit(i, (0,0))
all_ships[3]["image"].blit(i, (0,0))
all_ships[4]["image"].blit(i, (0,0))

def move_ship(ship):
  if ship["forward"]:
    ship["rect"].move_ip(ship["speed"], 0)
  else:
    ship["rect"].move_ip(-ship["speed"], 0)

def bounce_ship(ship):
  if ship["rect"].x > 720 - ship["rect"].w:
    ship["forward"] = False
  elif ship["rect"].x < 0:
    ship["forward"] = True

while True:
  clock.tick(FPS)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

  for ship in all_ships:
    move_ship(ship)

  for ship in all_ships:
    bounce_ship(ship)
  
  screen.fill(BLACK)

  for ship in all_ships:
    if ship["forward"]:
      screen.blit(pygame.transform.rotate(ship["image"], 90), ship["rect"])
    else:
      screen.blit(pygame.transform.rotate(ship["image"], -90), ship["rect"])

  pygame.display.update()
  
  
 
