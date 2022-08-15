import random

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
    winner = 'wrong'
  return winner

print('1. Rock')
print('2. Paper')
print('3. Scizzors')

def rsp123(bot):
  rsp = 'g'
  if bot == 1:
    rsp = "The rock"
  if bot == 2:
    rsp = "paper"
  if bot == 3:
    rsp = "cutter"
  return rsp

amugs = True

def rpz1p():
 while amugs == True:
  player = input('Choose ')
  bot = (random.randint(1, 3))
  print(f'The bot choosed: {rsp123(bot)}!')
  #print(winner(player, bot), "won!")
  if winner(player, bot) == "tie":
    print('itz a tie')
  elif winner(player, bot) == 'bot':
    print('the bot won LLL')
  elif winner(player, bot) == 'player':
    print('to ez huh')
  else:
    print(gigigiav)
  again = input('Wanna play again?yes/no: ')
  if again == 'no':
    print('bye')
    amugos = False
  else:
    print('lets play again')


rpz1p()


#def rpz2p():
 # rpz = (random.randint(1, 3))
 # player = input("")




