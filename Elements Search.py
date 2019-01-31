class work:
    @staticmethod
    def search(array,no):
        p = 0
        for x in range(len(array)) :
             if array[x] == no:
                 p = 1
                 place = x

        if p == 1:
            print("No. is found at {} location".format(place+1))
        else:
            print("No.is not found")

aayush = work()

array = []
inp = int(input("How many numbers do you want to input : \n"))

print("Enter your numbers now")

for x in range(inp):
    array.append(int(input("{}:\n".format(x+1))))

z = int(input("Enter the number you want to find: \n"))
aayush.search(array,z)

