class aayush:

    @staticmethod
    def pnhn(array1,array2):

        finalarray = []

        for x in array1:
            for y in array2:
                if x == y:
                    finalarray.append(x)

        print("{} \n ".format(finalarray))


aayushx = aayush()



with open('primenumbers.txt','r') as open_1:
    a1 = open_1.readlines()

with open('happynumbers.txt','r') as open_2:
    a2 = open_2.readlines()

aayushx.pnhn(a1,a2)
