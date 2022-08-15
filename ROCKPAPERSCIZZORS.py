import random

def gm(gamemode):
  gamemode = input("1 player or 2? 1/2: ")
  if gamemode == 2:
    rpz2p()
  else:
    rpz1p()




def winner(player, bot):
  winner = None
  if player == '1' and bot == 1:
    winner = 'tie'
  elif player == '1' and bot == 2:
    winner = 'bot'
  elif player == '1' and bot == 3:
    winner = 'player'
  elif player == '2' and bot == 1:
    winner = 'player'
  elif player == '2' and bot == 2:
    winner = 'tie'
  elif player == '2' and bot == 3:
    winner = 'bot'
  elif player == '3' and bot == 1:
    winner = 'bot'
  elif player == '3' and bot == 2:
    winner = 'player'
  elif player == '3' and bot == 3:
    winner = 'player'
  else:
   winner = 'invalid input'
  return winner

print('1. Rock')
print('2. Paper')
print('3. Scizzors')

def rps123(bot):
  if bot == 1:
    bot = 'The Rock'
  elif bot == 2:
    bot = 'papel'
  elif bot == 3:
    bot = 'Scizzors'
  return bot

def rpz1p():
 amugos = True
 while amugos == True:
  player = input('Choose ')
  bot = random.randint(1, 3)
  print(f'The bot choosed:{rps123(bot)}!')
  if winner(player, bot) == 'bot':
    print('The bot won!')
  elif winner(player, bot) == 'player':
    print('The player won!')
  elif winner(player, bot) == 'tie':
    print('Its a tie!')
  else:
    print(winner(player, bot))
  again = input('Wanna play again?yes/no: ')
  if again == 'no':
    print('bye')
    amugos = False
  else:
    print('lets play again')


def rpz1p():
 amugos = True
 while amugos == True:
  player = input('Choose ')
  bot = random.randint(1, 3)
  print(f'The bot choosed:{rps123(bot)}!')
  if winner(player, bot) == 'bot':
    print('The bot won!')
  elif winner(player, bot) == 'player':
    print('The player won!')
  elif winner(player, bot) == 'tie':
    print('Its a tie!')
  else:
    print(winner(player, bot))
  again = input('Wanna play again?yes/no: ')
  if again == 'no':
    print('bye')
    amugos = False
  else:
    print('lets play again')

