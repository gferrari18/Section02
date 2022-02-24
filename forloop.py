phr = input("Enter a phrase: ")
alpha = 0
numeric = 0

for x in phr:
    if x.isalpha():
        alpha = alpha + 1
    if x.isnumeric():
        numeric = numeric + 1

print("we went through phrase and...")
print("It contains " + str(alpha) + " letters")
print("it contains " + str(numeric) + " numbers")