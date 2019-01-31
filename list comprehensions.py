class work:

    @staticmethod
    def comprehensions(array1,array2):
        g = 1
        l = 0
        answer = []
        answer1 = []
        for x in array1:
            for y in array2:
                if x == y:
                    answer1.append(x)



        print(set(answer1))


action = work()
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

work.comprehensions(a,b)


