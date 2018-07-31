answer = input("How many times do I have to tell you? ")
answer = int(answer)

for time in range(answer):
  print("Hello.")

for num in range(1,21):
  if num == 4:
    print("4 is unlucky")
  elif num == 13:
    print("13 is unlucky")
  elif num % 2 == 0:
    print(f"{num} is even")
  elif num % 2 > 0:
    print(f"{num} is odd")

for num in range(1,21):
  if num == 4 or num == 13:
    print(f"{num} is unlucky")
  elif num % 2 == 0:
    print(f"{num} is even")
  else:
    print(f"{num} is odd")
  
for num in range(1,21):
  if num == 4 or num == 13:
    state = "unlucky"
  elif num % 2 == 0:
    state = "even"
  else:
    state = "odd"
  print(f"{num} is {state}")
