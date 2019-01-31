import random

class work:
    cows = 0
    bulls = 0
    randn = 0
    def random(self):
        self.randn = random.randint(1000, 9999)
        return self.randn

    def cab(self,no,randno):
        self.cows = 0
        self.bulls = 0
        one = no%10
        tenth = no%100 - one
        hundreth = no%1000 - (tenth+one)
        thousandth = no - (hundreth+tenth+one)

        rone = randno%10
        rtenth = randno%100 - rone
        rhundreth = randno%1000 - (rtenth+rone)
        rthousandth = randno - (rhundreth+rtenth+rone)

        if thousandth == rthousandth:
            self.cows += 1
        else:
            self.bulls +=1
            print("Hint: Guess the first Digit Correctly")

        if hundreth == rhundreth:
            self.cows += 1
        else:
            self.bulls +=1
            print("Hint: Guess the second Digit Correctly")

        if tenth == rtenth:
            self.cows += 1
        else:
            self.bulls +=1
            print("Hint: Guess the third Digit Correctly")



        if one == rone:
            self.cows += 1
        else:
            self.bulls +=1
            print("Hint: Guess the fourth Digit Correctly.")





print("Welcome to the Game of cows and bulls!!")
x = int(input("Guess a 4 digit number :\n"))

work1 = work()

init = work1.random()
work1.cab(x,init)

while(x != init):
    print("{} Cows, {} Bulls ".format(work1.cows,work1.bulls ))
    x = int(input("Again Guess a Number: \n"))
    work1.cab(x, init)

print("You have guessed the correct number. Nice Job!")