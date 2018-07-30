from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Make your move: ").lower()
rand_num = randint(0,2)

if rand_num == 0:
  computer = "rock"
elif rand_num == 1:
  computer = "scissors"
else:
  computer = "paper"
print(f"Computer plays {computer}...")


if player == computer:
  print("It's a tie!")
elif player == "rock":
  if computer == "scissors":
    print("You win!")
  if computer == "paper":
    print("Computer wins!")
elif player == "paper":
  if computer == "rock":
    print("You win!")
  if computer == "scissors":
    print("Computer wins!")
elif player == "scissors":
  if computer == "paper":
    print("You win!")
  elif computer == "rock":
    print("Computer wins!")
else:
  print("Something went wrong.")
