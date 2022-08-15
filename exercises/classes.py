class Something:
  speed = 88

# Skapa ett objekt av klassen `Something`
s1 = Something()

# Fråga efter objektets hastighet
print(s1.speed)

# Man kan lägga till egenskaper
s1.name = "Brian Gables"



class Person:
  # När vi definierar `__init__` ser vi till att de skapade objekten alltid har
  # en viss egenskap
  def __init__(objektetSomSkapas, n):
    objektetSomSkapas.name = n

class Car:
  # Objektet som skapas brukar kallas `self`
  def __init__(self, n):
    self.name = n

p1 = Person("Håkan")
p2 = Person("Frank")

c1 = Car("Opel")

def printName(p):
  print(p.name)

printName(s1)
printName(p1)
printName(p2)
printName(c1)

# `printName` på ett objekt som inte har attributet `name` är inte tillåtet
# printName(777)
