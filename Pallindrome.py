
class work:
    @staticmethod
    def palindrome(name):
        i = 0
        dec = 1
        x = 0
        y = 0

        original = list(name)

        i = len(original)

        for y in range(i):
            if original[y] != original[i - y - 1]:
                dec = 0

        if dec == 1:
            print("String is palindrome")

        else:
            print("String is not palindrome")


work1 = work()

exit = input("Enter to check whether a number is palindrome or not: \n")

work1.palindrome(exit)








