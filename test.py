import os

def clearScreen():
  os.system('cls')

# Takes a list of three elements (`boxes`) and draws the corresponding row. The
# result is represented as a string.
#
# Exampel:
#
#     drawRow(["*", "O", "*"]) = "| *  O  * |"
#     drawRow(["1", "2", "3"]) = "| 1  2  3 |"
def drawRow(boxes):
  return f"| {boxes[0]}  {boxes[1]}  {boxes[2]} |"

# (String, [String1]9) -> String
def drawPlane(title, boxes):
  return (
    # " " + title + "\n" +
    f" {title}\n" +
    ",---------,\n" +
    drawRow([boxes[0], boxes[1], boxes[2]]) + "\n" +
    drawRow([boxes[3], boxes[4], boxes[5]]) + "\n" +
    drawRow([boxes[6], boxes[7], boxes[8]]) + "\n" +
    "'---------'\n"
  )

noValidPositionMessage = "That's no valid position."

# ([String1]9, int, String1) -> String or None
def place(spelplan, position, newElement):
  if position > 9 or position < 1:
    return noValidPositionMessage
  elif spelplan[position-1] != " " and allFull(spelplan):
    return "That position is occupied."
  else:
    spelplan[position-1] = newElement
      # The result is always None if there is no return statement

# [String1] -> Bool
def allFull(boxes):
  fullSoFar = True
  for box in boxes:
    fullSoFar = fullSoFar and box != " "
  return fullSoFar

# ([String1]3, String1) -> Bool
def winningLine(line, player):
  return line[0] == player and line[1] == player and line[2] == player

# ([String1]9, String1) -> Bool
def anyWinningLine(Gameboard, player):
  winning = winningLine([Gameboard[0], Gameboard[1], Gameboard[2]], player) or \
            winningLine([Gameboard[3], Gameboard[4], Gameboard[5]], player) or \
            winningLine([Gameboard[6], Gameboard[7], Gameboard[8]], player) or \
            winningLine([Gameboard[0], Gameboard[3], Gameboard[6]], player) or \
            winningLine([Gameboard[1], Gameboard[4], Gameboard[7]], player) or \
            winningLine([Gameboard[2], Gameboard[5], Gameboard[8]], player) or \
            winningLine([Gameboard[0], Gameboard[4], Gameboard[8]], player) or \
            winningLine([Gameboard[2], Gameboard[4], Gameboard[6]], player)
  return winning

# String1 -> String1
def flipPlayer(player):
  if player == "B":
    nextPlayer = "O"
  else:
    nextPlayer = "B"
  return nextPlayer

def printErrorTryAgain(errorMsg):
  print(f"Oops! {errorMsg} Try again\n")

def game():
  Gameboard = [" "] * 9
  player   = "B"
  while True:
    print(drawPlane("Gameboard", Gameboard))
    print(f"Player {player} where do you wanna put ya balls?")

    # The `int` function will throw a `ValueError` if the input is not an
    # integer. The `except` block catches the error so that the program can
    # continue.
    #
    # We need to put `except` after the `if` statement, because the `if`
    # statement should not be run if the input gives a `ValueError`. (The player
    # should not be flipped when there's an error.)
    try:
      svar = int(input())
      message = place(Gameboard, svar, player)

      # If `message` is a string, it means that something went wrong
      if type(message) == str:
        clearScreen()
        printErrorTryAgain(message)
      elif anyWinningLine(Gameboard, player):
        clearScreen()
        print(drawPlane("Gameboard", Gameboard))
        print(f"Congrats player {player} yo've won!")
        break
      elif allFull(Gameboard):
        clearScreen()
        print(drawPlane("Gameboard", Gameboard))
        print("Its a tie(")
        break
      else:
        player = flipPlayer(player)
        clearScreen()
    except (ValueError):
      clearScreen()
      printErrorTryAgain(noValidPositionMessage)

game()
