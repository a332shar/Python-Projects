class work:

    @staticmethod
    def prime(aayush):
        dec = 0
        for x in range(2,(aayush-1)):
            if aayush%x == 0:
                dec = 1

        if dec == 1:
            print("No. is composite or not prime")


        else:
            print("No. is prime")



work1 = work()

lol = int(input("Enter a number to check whether it's prime or composite:\n"))

work1.prime(lol)



