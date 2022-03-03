import random

def getOperator(): #gets operator

  operator = random.choice("+-*/")
  return operator



def randomNumber(): #generates random numbers
  number = random.randint(1,100)
  return number


questionId = 1
corrects = 0
while questionId <= 10:
  numberOne = randomNumber()
  numberTwo = randomNumber()
  numberThree = randomNumber()
  op = getOperator()
  op2 = getOperator()
  question = (str(numberOne) + op + str(numberTwo)) + op2 + str(numberThree)
  result = round(eval(question))
  print("What is the answer for the following question?")
  print("Question " + str(questionId) + ":" + "(" +str(numberOne) + str(op) + str(numberTwo)+ ")" + str(op2) + str(numberThree))
  print(result)
  ans = int(input("Your answer is: "))
  print("aaa:" + str(ans))
  
  if ans == result:
    corrects = corrects + 1
  questionId = questionId + 1
  print("You answered a total of "+ str(corrects) + " questions")
