class work:

    @staticmethod
    def startend(array1):
        a = []
        start = array1[0]
        end = array1[len(array1)-1]

        a.append(start)
        a.append(end)

        print(a)

aayush = work()
b = [-1,-34,5, 10, 15, 20, 25,30,27,34]

aayush.startend(b)
