# Same as TickTackToe.py but uses custom classes to represent X and O.

import os

def clearScreen():
  os.system('cls')


##### Alt 1

class Player:
  def __init__(self, m):
    if (m != "X" and m != "O"):
      raise Exception("Player marker must be X or O")
    self.marker = m

player1 = Player("X")
player2 = Player("O")



##### Alt 2

class X:
  marker = "X"

class O:
  marker = "O"

player3 = X()
player4 = O()



print(player1.marker)
print(player2.marker)
print(player3.marker)
print(player4.marker)







# # Takes a list of three elements (`boxes`) and draws the corresponding row. The
# # result is represented as a string.
# #
# # Exampel:
# #
# #     drawRow(["*", "O", "*"]) = "| *  O  * |"
# #     drawRow(["1", "2", "3"]) = "| 1  2  3 |"
# def drawRow(boxes):
#   return f"| {boxes[0]}  {boxes[1]}  {boxes[2]} |"
#
# # (String, [String1]9) -> String
# def drawPlane(title, boxes):
#   return (
#     # " " + title + "\n" +
#     f" {title}\n" +
#     ",---------,\n" +
#     drawRow([boxes[0], boxes[1], boxes[2]]) + "\n" +
#     drawRow([boxes[3], boxes[4], boxes[5]]) + "\n" +
#     drawRow([boxes[6], boxes[7], boxes[8]]) + "\n" +
#     "'---------'\n"
#   )
#
# noValidPositionMessage = "That's no valid position."
#
# # ([String1]9, int, String1) -> String or None
# def place(list, position, newElement):
#   if position > 9 or position < 1:
#     return noValidPositionMessage
#   elif list[position-1] != " ":
#     return "That position is occupied."
#   else:
#     list[position-1] = newElement
#       # The result is always None if there is no return statement
#
# # [String1] -> Bool
# def allFull(boxes):
#   fullSoFar = True
#   for box in boxes:
#     fullSoFar = fullSoFar and box != " "
#   return fullSoFar
#
# # ([String1]3, String1) -> Bool
# def winningLine(line, player):
#   return line[0] == player and line[1] == player and line[2] == player
#
# # ([String1]9, String1) -> Bool
# def anyWinningLine(spelplan, player):
#   winning = winningLine([spelplan[0], spelplan[1], spelplan[2]], player) or \
#             winningLine([spelplan[3], spelplan[4], spelplan[5]], player) or \
#             winningLine([spelplan[6], spelplan[7], spelplan[8]], player) or \
#             winningLine([spelplan[0], spelplan[3], spelplan[6]], player) or \
#             winningLine([spelplan[1], spelplan[4], spelplan[7]], player) or \
#             winningLine([spelplan[2], spelplan[5], spelplan[8]], player) or \
#             winningLine([spelplan[0], spelplan[4], spelplan[8]], player) or \
#             winningLine([spelplan[2], spelplan[4], spelplan[6]], player)
#   return winning
#
# # String1 -> String1
# def flipPlayer(player):
#   if player == "X":
#     nextPlayer = "O"
#   else:
#     nextPlayer = "X"
#   return nextPlayer
#
# def printErrorTryAgain(errorMsg):
#   print(f"Oops! {errorMsg} Try again\n")
#
# def game():
#   spelplan = [" "] * 9
#   player   = "X"
#   while True:
#     print(drawPlane("Spelplan", spelplan))
#     print(f"Spelare {player} var vill du lägga nästa?")
#
#     # The `int` function will throw a `ValueError` if the input is not an
#     # integer. The `except` block catches the error so that the program can
#     # continue.
#     #
#     # We need to put `except` after the `if` statement, because the `if`
#     # statement should not be run if the input gives a `ValueError`. (The player
#     # should not be flipped when there's an error.)
#     try:
#       svar = int(input())
#       message = place(spelplan, svar, player)
#
#       # If `message` is a string, it means that something went wrong
#       if type(message) == str:
#         clearScreen()
#         printErrorTryAgain(message)
#       elif anyWinningLine(spelplan, player):
#         clearScreen()
#         print(drawPlane("Spelplan", spelplan))
#         print(f"Grattis spelare {player} du vann!")
#         break
#       elif allFull(spelplan):
#         clearScreen()
#         print(drawPlane("Spelplan", spelplan))
#         print("Det blev oavgjort :(")
#         break
#       else:
#         player = flipPlayer(player)
#         clearScreen()
#     except (ValueError):
#       printErrorTryAgain(noValidPositionMessage)
#
# game()
