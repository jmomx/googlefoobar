
# turn a n-digit number into a 1 digit number
# by recursively adding the digits

def answer(x):
    sum = 0
    xstr = str(x)
    for c in list(xstr):
        sum += int(c)
    if sum < 10:
        return sum
    else:
        return answer(sum)


def main():
    print answer(1235)
    print answer(12356)
    print answer(12357)

if __name__ == "__main__": main()
