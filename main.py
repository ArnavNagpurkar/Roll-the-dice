import random

print("--------------")
print("Dice simulator")
print("--------------")


def diceNum():
  num = random.randint(1, 6)
  print(f"\nYour number that rolling dice has selected is \"{num}\" ")
  again = input("\nRoll dice again? (Y/N):")
  if again == "Y" or again == "y":
    diceNum()
  elif again == "N" or again == "n":
    print("\nThanks for rolling the dice\nExiting...!")
    exit()
  else:
    print("Exiting...!")
    exit()


diceNum()
