import numpy as np
from copy import deepcopy
from heapq import *
from collections import deque
inp_st = input("Enter the inital state:")

goal_st = input("Enter the goal state:")
a=np.array(list(map(int, inp_st)))
a=np.reshape(a,(3,3))

G=np.array(list(map(int, goal_st)))
G=np.reshape(G,(3,3))

choice = input("Enter the choice ManhattanDistance:1 or MisplacedTiles:0")
nodeid=0
open=[]                       # Open nodes will be stored in this list
closed=[]# Closed nodes will be stored in this list
lnkd_lst=[]
def nextnodes(x):                # To geneerate all the possible child states of a current state
    currentstate = np.array(x[4])                       #fn,gn,nodeid,parentid,node
    g=x[1]+1
    global nodeid
    parentid=x[2]
    h=calculateManhattanDistance(currentstate,G)   #Manhattan distance between current and goal states
    e = ['up', 'down', 'left', 'right']             #Possible directions in which 0 can be moved
    a = np.where(currentstate == 0)
    for i in e:
        c = deepcopy(currentstate)
        parity = 0
        if i == 'up':
            if (a[0] != 0):
                c[a[0], a[1]], c[a[0] - 1, a[1]] = c[a[0] - 1, a[1]], c[a[0], a[1]]

                for j in closed:
                    if np.array_equal(np.array(j[4]),np.array(c)):
                        parity =3
                        break

                for j in open:
                    if np.array_equal(np.array(j[4]),np.array(c)):
                        parity =3
                        break

                if(parity == 0):
                    nodeid=nodeid+1
                    if(choice=='1'):
                     temp=(g+calculateManhattanDistance(np.array(c),G),g,nodeid,parentid,c)
                    if(choice=='0'):
                      temp=(g+calculateMisplacedTiles(np.array(c),G),g,nodeid,parentid,c)
                    heappush(open,temp) #storing the generated state in a heap data structure

        if i == 'down':
            if (a[0] != 2):
                c[a[0], a[1]], c[a[0] + 1, a[1]] = c[a[0] + 1, a[1]], c[a[0], a[1]]
                for j in closed:
                    if np.array_equal(np.array(j[4]), np.array(c)):
                        parity = 3
                        break
                for j in open:
                    if np.array_equal(np.array(j[4]), np.array(c)):
                        parity = 3
                        break
                if (parity == 0):
                    nodeid = nodeid + 1
                    if (choice == '1'):
                     temp = (g + calculateManhattanDistance(np.array(c), G), g, nodeid, parentid, c)
                    if(choice == '0'):
                        temp = (g + calculateMisplacedTiles(np.array(c), G), g, nodeid, parentid, c)
                    heappush(open, temp) #storing the generated state in a heap data structure
        if i == 'left':
            if (a[1] != 0):
                c[a[0], a[1]], c[a[0], a[1] - 1] = c[a[0], a[1] - 1], c[a[0], a[1]]
                for j in closed:
                    if np.array_equal(np.array(j[4]), np.array(c)):
                        parity = 3
                        break
                for j in open:
                    if np.array_equal(np.array(j[4]), np.array(c)):
                        parity = 3
                        break
                if (parity == 0):
                    nodeid = nodeid + 1
                    if (choice == '1'):
                     temp = (g + calculateManhattanDistance(np.array(c), G), g, nodeid, parentid, c)
                    if(choice =='0'):
                        temp = (g + calculateMisplacedTiles(np.array(c), G), g, nodeid, parentid, c)
                    heappush(open, temp) #storing the generated state in a heap data structure
        if i == 'right':
            if (a[1] != 2):
                c[a[0], a[1]], c[a[0], a[1] + 1] = c[a[0], a[1] + 1], c[a[0], a[1]]

                for j in closed:
                    if np.array_equal(np.array(j[4]), np.array(c)):
                        parity = 3
                        break
                for j in open:
                    if np.array_equal(np.array(j[4]), np.array(c)):
                        parity = 3
                        break
                if (parity == 0):
                    nodeid = nodeid + 1
                    if (choice == '1'):
                     temp = (g + calculateManhattanDistance(np.array(c), G), g, nodeid, parentid, c)
                    if(choice == '0'):
                        temp = (g + calculateMisplacedTiles(np.array(c), G), g, nodeid, parentid, c)
                    heappush(open, temp) #storing the generated state in a heap data structure


def calculateManhattanDistance(Temp_Int, Goal):        #Calculate the manhattan distance between each state generated and the Goal state
    manhattanDistanceSum = 0;
    for p in range(0, 3, 1):
        for q in range(0, 3, 1):
            value = Temp_Int[p][q]
            for m in range(0, 3, 1):
                for n in range(0, 3, 1):
                    if (Goal[m][n] == value and Goal[m][n] != 0):
                        a = abs(p - m)
                        b = abs(q - n)
                        c = a + b
                        manhattanDistanceSum += c
    manhattanDistance = manhattanDistanceSum

    return manhattanDistance

def calculateMisplacedTiles(Temp_Int,Goal):
    misplacedsum=0
    for p in range(0,3,1):
        for q in range(0,3,1):
            value=Temp_Int[p][q]
            if(Goal[p][q]!=value & value!=0):
                        misplacedsum+=1
    return misplacedsum


def findpath(Pop_Node):                            # Storing the states from Initial state to Goal state
    k=np.array(Pop_Node[4])
    l=Pop_Node[2]
    x=Pop_Node[3]
    g=[(l,k)]

    print(open,'\n')
    print(closed,'\n')

    for nn in g:
        heappush(lnkd_lst, nn)
    while True:
        if x == -1:
            break
        for i in open:
            if i[2]==x:
                p=(i[2],i[4])
                heappush(lnkd_lst, p)
                x=i[3]
                break
        for j in closed:
            if j[2]==x:
                p = (j[2], j[4])
                heappush(lnkd_lst, p)
                x=j[3]
                break

def main():
    b = a
    b = np.reshape(b, (3, 3))     #Reshaping the Initial state to 3 by 3
    mhn_initialnode=calculateManhattanDistance(b,G)
    initialnode=[(mhn_initialnode,0,0,-1,b)]   #fn,gn,nodeid,parentid,node

    for i in initialnode:
        heappush(open, i)        #storing the initial state in a heap data structure


    while True:                  #np.array_equal(open[0][4],G)
        if(len(open)+len(closed)>8000):  #limiting the count of total nodes geenerated to 8000
            print("no solution")
            return
        Pop_Node=heappop(open)
        Sel_Node=Pop_Node[4]
        Exp_nodes=Pop_Node[3]
        Path_Cost=Pop_Node[1]
        Sel_Node=np.array(Pop_Node[4])
        if(np.array_equal(Sel_Node,G)):   #Checking if the state in heap matched the Goal State
            print('found')
            print("nodes generated :",nodeid)
            print("nodes expanded:",len(closed))
            print("path cost:",Path_Cost)
            findpath(Pop_Node)       # Storing the states from Initial state to Goal state in a heap once the goal is reached
            break
        heappush(closed,Pop_Node)
        nextnodes(Pop_Node)

    while len(lnkd_lst)!=0:          #To print the states used to reach the goal state
        Temp_lnkd_lst=heappop(lnkd_lst)
        Temp_lnkd_lst=Temp_lnkd_lst[1]
        print(Temp_lnkd_lst,'\n')



 #popvalue from open check for goal
    #send poped node to next nodes
#send this node to closed

if __name__ == '__main__':
    main()

