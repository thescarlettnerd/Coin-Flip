import random
print("Welcome to the coin flipper.")
call = input("Please call HEADS or TAILS:\n")
flip = random.randint(0, 1)
if flip == 1 and call.lower() == "heads":
  print("Heads, you win.")
elif flip == 1 and call.lower() == "tails":
  print("Heads, you lose.")
elif flip == 0 and call.lower() == "heads":
  print("Tails, you lose.")
elif flip == 0 and call.lower() == "tails":
  print("Tails, you win.")