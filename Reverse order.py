class work:

    @staticmethod
    def reverse(line):
        straight = line.split(" ")
        x = 0
        while x != int(len(straight)/2):
            temp = straight[x]
            straight work
            straight[(len(straight) - x) - 1] = temp

            x += 1


        answer = " ".join(straight)
        return answer


work9 = work()
inp = input("Enter the string you want to reverse: \n")

result = work9.reverse(inp)
print(result)
