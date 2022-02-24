

year = input("How old are you? ")

while year.isnumeric() == False or int(year) <= 0:
    print("Invalid! Enter your age as a number above 0")
    year = input("How old are you? ")


if int(year) == 1:
    print("You are " + year + " year old!")
else:  print("You are " + year + " years old!")