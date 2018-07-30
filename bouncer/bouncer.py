age = input("What is your age? ")

if age:
  age = int(age)
  if age >= 18 and age < 21:
    print("You can enter, but need a wristband.")
  elif age >= 21:
    print("You can enter and drink.")
  else:
    print("Too young.")
else:
  print("Please enter your age.")
  