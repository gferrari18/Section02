def sumofdigits(n):
    sum = 0
    for x in n:
        if x.isdigit() == True:
            z = int(x)
            sum = sum + z
    return sum

phrase = input("tell me a phrase that contains digits: ")
print("We added all of the digits in your phrase and you have a total of: ")
print(sumofdigits(phrase))