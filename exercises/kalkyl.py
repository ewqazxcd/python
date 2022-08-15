import random



def add (x, y):
  return x + y

def sub (x, y):
  return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

while True:
  doin = input("watcha gonna do now 1 2 3 or 4: ")
  quote = (random.randint(0,1))
  if quote == 0:
    print("awmwgus")
  else:
    print('afungus')
  try:
    if doin in ('1', '2', '69','mimimi', '3', '4'):
      num1 = float(input("first doin\n"))
      num2 = float(input("after doin\n"))
      #num3 = float(input("first doin\n"))
      #num4 = float(input("first doin\n"))
      if doin == 'mimimi':
        print("mimimi")
      elif doin == '1':
        print("itz", add(num1, num2))
      elif doin == '2':
        print('itz', sub(num1, num2))
      elif doin == '3':
        print('itz', mul(num1, num2))
      elif doin == '4':
        print('itz', div(num1, num2))
      else:
        print("gigiggigaw")
    else:
        print("nob")
  except (ValueError):
    print("why men")
