

def addsum(n):
    sum = 0
    for x in range(1, n+1):
        sum = sum + x
    return sum
   
def factorial(n):
    fac = 1
    for x in range(1, n+1):
       fac = fac * x
    return fac


n = int(input('enter a number: '))
print('sum from 1 to ' + str(n) + ' is ' + str(addsum(n)))
print("The factorial of " + str(n) + ' is ' + str(factorial(n)))