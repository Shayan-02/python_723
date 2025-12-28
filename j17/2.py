from random import randint

def guessNumber(hads):
  global c
  c = 1
  if hads > correctNumber:
    print("say lower");
  elif hads < correctNumber:
    print("say higher")
  else:
    print("you win")
    c = 0


start = int(input())
end = int(input())
correctNumber = randint(start, end)
# correctNumber = randint(10, 20)
# correctNumber = 15


for i in range(5):
  # hads = int(input("enter a number between {} to {}: ".format(start, end)))
  hads = int(input(f"enter a number between {start} to {end}: "))
  guessNumber(hads)
  if c == 0:
    break
else:
  print("you loss, correct number is", correctNumber)