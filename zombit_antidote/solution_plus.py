#zombit antidote

import random

# Node class used in old graph answer
class Node:


    def __init__(self, startandend):
        self.start = startandend[0]
        self.end = startandend[1]
        self.edges = []

    def add_edge(self, othernode):
        self.edges.append(othernode)

    def num_edges(self):
        return len(self.edges)


    def join(node, othernode):
        if node.start < othernode.end:
            if node.end > othernode.start:
                #conflict => edge
                node.add_edge(othernode)
                othernode.add_edge(node)
            else:
                #then the appt is just completely after
                return
        elif node.end > othernode.start:
            if node.start < othernode.end:
                #conflict => edge
                node.add_edge(othernode)
                othernode.add_edge(node)
            else:
                #then the appt is just before
                return

    def split(node, othernode):
        for edge in node.edges:
            if edge == othernode:
                node.edges.remove(othernode)
                othernode.edges.remove(node)

    def __str__(self):
        return ("(Node -> Start: " + str(self.start) + " | End: " + str(self.end) +
            " | Edges: " + str(self.num_edges()) + ")"+ super.__str__(self))


# Node class used in old graph answer
class Graph:

    def __init__(self):
        self.nodes = []

    def add(self, newnode):
        for node in self.nodes:
            #print self.nodes
            Node.join(node, newnode)
        self.nodes.append(newnode)

    def remove(self, oldnode):
        for node in self.nodes:
            if node == oldnode:
                #we found the node we want to remove
                self.nodes.remove(oldnode)
            else:
                #we found another node, possible connected to oldnode
                Node.split(node, oldnode)

    #def __str__(self):
    #    stringrep = "Graph -> Size: " + str(len(self.nodes))

# Graph based answer - incorrect first attempt
def old_answer(meetings):
    #create graph of meetings
    g = Graph()
    for meeting in meetings:
        g.add(Node(meeting))
    #now, prune graph into separate subgraphs
    #discrete subgraph implies an appt you can defintely make
    gsorted = sorted(g.nodes, key=Node.num_edges)
    while gsorted[-1].num_edges() > 0:
        #then there are still conflicts on the schedule
        #remove the appt with the most conflicts
        g.remove(gsorted[-1])
        #and try again
        gsorted = sorted(g.nodes, key=Node.num_edges)
    return len(g.nodes)


def answer(meetings):
    sortedms = sorted(meetings, key = end)
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

# Helper functions to make new answer look a little cleaner

def end(x):
    return x[1]

def start(x):
    return x[0]

############################

# Test Code

def testnode():
    a = Node([1,3])
    b = Node([2,4])
    c = Node([0,1])
    Node.join(a,b)
    Node.join(b,c)
    Node.join(a,c)
    Node.split(a,c)
    #Node.split(a,b)
    for d in [a,b,c]:
        print(d)

def testgraph():
    g = Graph()
    meetings = [[4,5], [0, 1], [1, 2], [2, 3], [3, 5]]
    for meeting in meetings:
        g.add(Node(meeting))
    #print len(g.nodes)
    for node in g.nodes:
        print (node)
    gsorted = sorted(g.nodes, key=Node.num_edges)
    print (" -- sorted --")
    for node in gsorted:
        print (node)
    print (" -- last node -- ")
    print (gsorted[-1])
    g.remove(gsorted[-1])
    print (" -- last node removed -- ")
    for node in g.nodes:
        print (node)

def testanswer():
    meetings = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]
    print ("Expected 4. Actual: " + str(answer(meetings)))
    meetings = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
    print ("Expected 5. Actual: " + str(answer(meetings)))
    meetings = [[0, 1], [0, 2], [2, 3], [3, 4], [4, 5]]
    print ("Expected 4. Actual: " + str(answer(meetings)))
    meetings = [[0, 1], [1, 2], [0, 3], [3, 4], [4, 5]]
    print ("Expected 4. Actual: " + str(answer(meetings)))
    meetings = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]
    print( "Expected 1. Actual: " + str(answer(meetings)))
    meetings = [[7,12], [1,3], [8,9], [15,17], [3,8], [11,16]]
    print ("Expected 4. Actual: " + str(answer(meetings))
    )

def compareanswer():
    for i in range(0,100000):
        meetings = generatemeetings()
        ans = answer(meetings)
        old_ans = old_answer(meetings)
        if ans != old_ans:
            print (meetings)
            print ("Answer: " + str(ans))
            print ("Old Answer: " + str(old_ans))
            return
    return


def generatemeetings():
    meetings = []
    for i in range(0,7):
        max_time = 100
        startval = random.randint(0,max_time)
        endval = random.randint(0,max_time)
        if startval > endval:
            meetings.append([endval,startval])
        elif endval < startval:
            meetings.append([startval, endval])
        else:
            meetings.append([startval, startval + 1])
    return meetings

def findbug():
    meetings = [[33, 98], [44, 47], [15, 65], [18, 19], [1, 52], [23, 40], [23, 49]]
    print(old_answer(meetings))

#############################


def main():
    #testnode()
    #testgraph()
    testanswer()
    #compareanswer()
    #findbug()


if __name__ == "__main__": main()
