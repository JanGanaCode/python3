# for number in range(1,11):
#   print (number)

for char in "hello":
  print(char)

n = range(0,10,2)
print(list(n))

for n in range(0,10,3):
  print(f"{n},")

num = 1
while num < 11:
  print(num)
  num += 1

answer = input("What is the password? ")
while answer != "password":
  print("Try again...")
  answer = input("What is the password? ")
print("Correct.")
