print("Welcome to Rock, Paper, Scissors!")
print("Rock = 1, Paper = 2, Scissors = 3")
usr = int(input("Enter your number: "))
import random
bot = random.randrange(1,4)

while usr < 1 or usr > 3:
    print("You need to chose a value between 1 and 3...")
    usr = int(input("Enter your number: "))


if usr == 1:
    print("You chose rock")
elif usr == 2:
    print('You chose paper')
elif usr == 3:
    print('You chose scissors')

if bot == 1:
    print("Bot chose rock")
elif bot == 2:
    print('Bot chose paper')
elif bot == 3:
    print('Bot chose scissors')


while usr == bot:
    print("Draw")
    print("You can't end on a tie")
    usr = int(input("Enter your number: "))
    bot = random.randrange(1,4)

if usr == 1 and bot == 2: print("You lose!")
if usr == 1 and bot == 3: print("You win!")
if usr == 2 and bot == 1: print('You win!')
if usr == 2 and bot == 3: print('You lose!')
if usr == 3 and bot == 1: print('You lose!')
if usr == 3 and bot == 2: print('You win!')
