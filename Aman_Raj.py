P1.
import random
def display(room):
    print(room)
room=[
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
    ]
print("All dirty rooms are")
display(room)
x=0
y=0
while x<4:
    while y<4:
        room[x][y]=random.choice([0,1])
        y+=1 
    x+=1 
    y=0
print("Random dirts detected")
display(room)
x=0
y=0
z=0
while x<4:
    while y<4:
        if room[x][y]==1:
            print("vaccum at location",x,y)
            room[x][y]=0
            print("cleaned",x,y)
            z+=1
        y+=1 
    x+=1 
    y=0
pro=(100-((z/16)*100))
print("cleaned,thanks:232")
display(room)
print("performance=",pro,"%")














P2.
#PQueue() functions
class PQueue():
    def __init__(self):
        self.dict = {}
        self.keys = []
        self.sorted = False
    #push fuction is used to push the keys into the stack with the given values. The push library is used
    def push(self, k, v):
        self.dict[k] = v
        self.sorted = False
    #sort fuction is used to sort the keys with the given values. The sort library is used
    def _sort(self):
        self.keys = sorted(self.dict, key=self.dict.get, reverse=True)
        self.sorted = True
    #pop fuction is used to pop the keys from the stack with the given values after sorting
    def pop(self):
        try:
            if not self.sorted:
                self._sort()
            key = self.keys.pop()
            value = self.dict[key]
            self.dict.pop(key)
            return key, value
        except:
            return None
# Heuristics function is used in uniform cost search and finds the most promissing path.
# #It takes the current state of the agent as its input and produces the estimation of how close agent is from the goal.
def heuristics(path):
    h = {}
    with open(path, 'r') as file:
        for line in file:
            k, v = line.split(", ")
            h[k] = int(v)
            print(h)
    return h

def path_costs(path):
    c = {}
    with open(path, 'r') as file:
        for line in file:
            line = line.split(", ")
            v = int(line.pop())
            e1 = line.pop()
            e2 = line.pop()
            if e1 not in c:
                c[e1] = {}
            if e2 not in c:
                c[e2] = {}
            c[e1][e2] = c[e2][e1] = v
            print(c)
    return c

def a_star(start, goal, h, g):
    frontier = PQueue()
    # pushing path and cost to pqueue
    frontier.push(start, h[start])
    while True:
        # poping path with least cost
        path, cost = frontier.pop()
        print(path+ " " +str(cost))
        # splitting out end node in path
        end = path.split("->")[-1]
        # removing heuristic value of end node from cost
        cost -= h[end]
        if goal == end:
            break
        for node, weight in g[end].items():
            # adding edge weight(cost) and node heuristic to total cost
            new_cost = cost + weight + h[node]
            new_path = path + "->" + node
            # adding new path and cost to pqueue
            frontier.push(new_path, new_cost) 
            

a_star('Arad', 'Bucharest', heuristics('./heuristics.txt'), path_costs('./path.txt'))




















P3.
from collections import defaultdict
class graph:
        def __init__(self,vertices):
            self.v=vertices
            self.graph=defaultdict(list)
            
        def addEdge(self,u,v):
            self.graph[u].append(v)
            
        def DLS(self,source,target,maxDepth):
            if source==target:return True
            if maxDepth<=0   :return False
            for i in self.graph[source]:
                if(self.DLS(i,target,maxDepth-1)):
                    return True
                return False
g=graph(9)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(2,6)
g.addEdge(3,7)
g.addEdge(3,8)

target=3
maxDepth=3
source=0
if g.DLS(source,target,maxDepth)==True:
    print("Target",target,"is reachable from source",source,"within maxDepth",maxDepth)
else:
    print("Target",target,"is not reachable from source",source,"within maxDepth",maxDepth)












p4.

class PQueue():
    def __init__(self):
        self.dict = {}
        self.keys = []
        self.sorted = False
    
    def push(self, k, v):
        self.dict[k] = v
        self.sorted = False
    
    def _sort(self):
        self.keys = sorted(self.dict, key=self.dict.get, reverse=True)
        self.sorted = True
 
    def pop(self):
        try:
            if not self.sorted:
                self._sort()
            key = self.keys.pop()
            value = self.dict[key]
            self.dict.pop(key)
            return key, value
        except:
            return None
 
def path_costs(path):
    c = {}
    with open(path, 'r') as file:
        for line in file:
            line = line.split(", ")
            v = int(line.pop())
            e1 = line.pop()
            e2 = line.pop()
            if e1 not in c:
                c[e1] = {}
            if e2 not in c:
                c[e2] = {}
            c[e1][e2] = c[e2][e1] = v
    return c
 
def ucs(start, goal, g):
    frontier = PQueue()
    # pushing path and cost to pqueue
    frontier.push(start, 0)
    while True:
        # poping path with least cost
        path, cost = frontier.pop()
        print(path+ " " +str(cost))
        # splitting out end node in path
        end = path.split("->")[-1]
        if goal == end:
            break
        for node, weight in g[end].items():
            # adding edge weight(cost) to total cost
            new_cost = cost + weight
            new_path = path + "->" + node
            # adding new path and cost to pqueue
            frontier.push(new_path, new_cost)      
 
ucs('Arad', 'Bucharest', path_costs('./path.txt'))







p5.
import math
import random
def minimax(currentdepth,nodeIndex,maxTurn,score,farDepth):
    if(currentdepth==farDepth):
        return score[nodeIndex]
    if(maxTurn):
        return max(minimax(currentdepth+1,nodeIndex*2,False,score,farDepth),minimax(currentdepth+1,nodeIndex*2+1,False,score,farDepth))
    else:return min(minimax(currentdepth+1,nodeIndex*2,False,score,farDepth),minimax(currentdepth+1,nodeIndex*2+1,False,score,farDepth))
score=random.sample(range(1,50),4)
print(str(score))
treeDepth=math.log(len(score),2)
print("The optimal value is:",end=" ")
print(minimax(0,0,True,score,treeDepth))

