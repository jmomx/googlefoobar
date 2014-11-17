#zombit antidote

def answer(meetings):
    sortedms = sorted(meetings, key=end)
    scheduledms = []
    for m in sortedms:
        conflict = False
        for scheduledm in scheduledms:
            if start(m) < end(scheduledm):
                if end(m) > start(scheduledm):
                    conflict = True
            elif end(m) > start(scheduledm):
                if start(m) < end(scheduledm):
                    conflict = True
        if not conflict:
            scheduledms.append(m)
    return len(scheduledms)


def end(x):
    return x[1]

def start(x):
    return x[0]


def main():
    testanswer()



def testanswer():
    meetings = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]
    print "Expected 4. Actual: " + str(answer(meetings))
    meetings = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
    print "Expected 5. Actual: " + str(answer(meetings))
    meetings = [[0, 1], [0, 2], [2, 3], [3, 4], [4, 5]]
    print "Expected 4. Actual: " + str(answer(meetings))
    meetings = [[0, 1], [1, 2], [0, 3], [3, 4], [4, 5]]
    print "Expected 4. Actual: " + str(answer(meetings))
    meetings = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]
    print "Expected 1. Actual: " + str(answer(meetings))
    meetings = [[7,12], [1,3], [8,9], [15,17], [3,8], [11,16]]
    print "Expected 4. Actual: " + str(answer(meetings))

if __name__ == "__main__": main()
