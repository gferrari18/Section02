
import random
bot = random.randrange(1,4)
usrscr = 0
botscr = 0
print("Welcome to Rock, Paper, Scissors!")

while usrscr < 7 and botscr < 7:
    bot = random.randrange(1,4)
    print("Rock = 1, Paper = 2, Scissors = 3")
    usr = int(input("Enter your number: "))

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
        print("Rock = 1, Paper = 2, Scissors = 3")
        usr = int(input("Enter your number: "))
        bot = random.randrange(1,4)

    if usr == 1 and bot == 2:
        print("You lose!")
        botscr = botscr + 1
       
    if usr == 1 and bot == 3:
        print("You win!")
        usrscr = usrscr + 1
      
    if usr == 2 and bot == 1:
        print('You win!')
        usrscr = usrscr + 1
       
    if usr == 2 and bot == 3:
        print('You lose!')
        botscr = botscr + 1
       
    if usr == 3 and bot == 1:
        print('You lose!')
        botscr = botscr + 1

    if usr == 3 and bot == 2:
        print('You win!')
        usrscr = usrscr + 1

    
    

if usrscr == 7:
    print("You won the game!")
else:
    print("You lost the game!")



