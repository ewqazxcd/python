# Uppgift att göra en simulerinhg av spelet snake

import random
import pygame
import pygame.freetype

pygame.init()

FONT = pygame.freetype.SysFont("Courier", 24)

# Skärmens storlek i orm-pluppar
WIDTH = 450
HEIGHT = 80

# Storleken på ormpluppen
PLUPP = 4

clock = pygame.time.Clock()
FPS = 50  # Frames per second.

BG_COLOR    = (0, 250, 200)
SNAKE_COLOR = (200, 100, 0)
HEAD_COLOR  = (200, 255, 0)

start_snake = [(0, 0), (1, 0), (2, 0)]

start_direction = "e"

def to_pixel(snake_coord):
  x = snake_coord[0]
  y = snake_coord[1]
  return (x*PLUPP, y*PLUPP)

screen = pygame.display.set_mode(to_pixel((WIDTH, HEIGHT)))

def next_pos(pos, d):
  x = pos[0]
  y = pos[1]

  if d == "n":
    return (x, y-1)
  elif d == "e":
    return (x+1, y)
  elif d == "s":
    return (x, y+1)
  elif d == "w":
    return (x-1, y)

def generate_fruit(snake):
  ok = False
  while(not(ok)):
    fruit = (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    if len(snake) == 200:
      ok = False
    else:
      ok = True
  return fruit

def points(snake):
  return len(snake) - 7

def start_screen():
  screen.fill(BG_COLOR)
  FONT.render_to(
    screen,
    (50, 250),
    "Press A For AFUNGUS AMOGUS ",
    (80, 5, 255),
    None,
    pygame.freetype.STYLE_STRONG,
    0,
    (60, 60)
  )
  pygame.display.update()

  keypressed = False

  while not(keypressed):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
          keypressed = True

  #screen.fill(BG_COLOR)
  #pygame.display.update()

def end_screen(snake):
  screen.fill(BG_COLOR)
  FONT.render_to(
    screen,
    (100, 250),
    "Amogus noob",
    (80, 5, 255),
    None,
    pygame.freetype.STYLE_STRONG,
    0,
    (60, 60)
  )
  FONT.render_to(
    screen,
    (270, 340),
    f"Score: {points(snake)}",
    (80, 5, 255),
    None,
    pygame.freetype.STYLE_STRONG,
    0,
    (30, 30)
  )
  pygame.display.update()
  pygame.time.delay(2000)

def game_loop(direction, snake):
  game_over = False

  fruit = (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
  pygame.event.clear()

  while not(game_over):
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          quit()
        elif event.key == pygame.K_LEFT:
          direction = "w"
        elif event.key == pygame.K_RIGHT:
          direction = "e"
        elif event.key == pygame.K_UP:
          direction = "n"
        elif event.key == pygame.K_DOWN:
          direction = "s"

    new_head = next_pos(snake[-1], direction)
    if new_head[0] < 0:
      game_over = True
    elif new_head[0] >= WIDTH:
      game_over = True
    elif new_head[1] < 0:
      game_over = Trueaa
    elif new_head[1] >= HEIGHT:
      game_over = True

    for segment in snake[1:]:
      if new_head == segment:
        game_over = True

    snake.append(new_head)
    generate_fruit(snake)

    old_head = snake[-2]
    old_tail = snake[0]

    if new_head == fruit:
      fruit = fruit + generate_fruit(snake) + generate_fruit(snake) + generate_fruit(snake) + generate_fruit(snake)
    else:
      snake.pop(0)

    pygame.draw.rect(screen, (255, 255, 0), (to_pixel(fruit), (PLUPP, PLUPP)))
    pygame.draw.rect(screen, BG_COLOR, (to_pixel(old_tail), (PLUPP, PLUPP)))
    pygame.draw.rect(screen, SNAKE_COLOR, (to_pixel(old_head), (PLUPP, PLUPP)))
    pygame.draw.rect(screen, HEAD_COLOR, (to_pixel(new_head), (PLUPP, PLUPP)))

    pygame.display.update()

  return snake

while True:
  start_screen()
  snake = game_loop(start_direction, start_snake.copy())
  end_screen(snake)
