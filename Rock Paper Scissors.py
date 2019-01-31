class work:

    @staticmethod

    def rps(input1,input2):
        if input1 == input2:
            print("It's a tie")

        elif input1 == "rock":
            if input2 == "scissors":
                print("Player 1 won")
            else:
                print("Player 2 won")

        elif input1 == "paper":
            if input2 == "scissors":
                print("Player 2 won")
            else:
                print("Player 1 won")


        elif input1 == "scissors":
            if input2 == "rock":
                print("Player 2 won")
            else:
                print("Player 1 won")

        else:
            print("Please enter a valid input from next time")

print("Welcome to the game of rock paper scissors")

decision1 = input("Enter inputpap for user 1:\n")
decision2 = input("Enter input for user 2:\n")

work1 = work()

work1.rps(decision1,decision2)

i = True
while(i == True):
    x = input("Do you want to play game again(Y/N):\n")
    if(x == "Y"):
        decision1 = input("Enter input for user 1:\n")
        decision2 = input("Enter input for user 2:\n")
        work1.rps(decision1, decision2)
    else:
        print("Thanks for playing game of rock paper scissors")
        i = False







