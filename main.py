from random import randint

while True:
    
    player = input("rock (r), paper (p) or scissors (s)? ")  #here player chooses one of them..
    print(player, 'vs', end=' ')

    chosen = randint(1,3)  #here computer chooses between rock, paper and scissors..

    if chosen == 1:
        computer = 'r'
    elif chosen == 2:
        computer = 'p'
    else:
        computer = 's'
    print(computer)


# code for deciding which wins...
    if computer == player:
        print("DRAW!!!!!")

    elif player == 'r' and computer == 'p':
        print("Computer wins!!!!")

    elif player == 'r' and computer == 's':
        print("Player wins!!!!")

    elif player == 'p' and computer == 'r':
        print("Player wins!!!!")

    else:
        #player == 'p' and computer == 's':
        print("Computer wins!!!!")


    user = input("Do you want to Quit(y/n)? ")
    if user == 'y':
        break
    
        
    
