class work:

    @staticmethod
    def write(name):
        with open('{}.txt'.format(name),'w') as aayush_file:
            aayush_file.write('It is such a good weather!')


work1 = work()

i = input("Enter the name of the File you want to add:\n")

work1.write(i)
