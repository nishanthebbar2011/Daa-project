class Node :
    def __init__(self,n,):
        self.number = n
        self.cost=0
from collections import defaultdict
# This class represents a directed graph using adjacency matrix representation
class Graph:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.org_graph = [i[:] for i in graph]
        self.ROW = len(graph)
        self.COL = len(graph[0])

    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''

    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    # Returns tne min-cut of the given graph
    def minCut(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        # print the edges which initially had weights

        print(max_flow)
        Final =[0 for i in range(sink+1)]
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == 0 and self.org_graph[i][j] > 0:
                    if (i!=0 and j!=0) or (i!=sink and j!=sink):
                        Final[i]=1
                        Final[j]=1


                    print (str(i) + " - " + str(j))
        Final[0]=0
        Final[sink]=0
        print("Projects to Be Chosen are : ")
        for i in range(len(Final)):
            if Final[i]==1:
                print(i)


print("Enter the Number of Projects")
n=int(input())
print("Enter the projects with their dependencies like 1 - 2 ")
print("That means 2 depends on 1 ")
Nodes=list()
Values=list()
capacitymatrix = [[0 for i in range(n+2)] for i in range(n+2)]



#enter -1 to quit
t=0
while(t!=-1):
    n1,n2=input().split(" ")
    if int(n1) == -1 and int(n2) == -1:
        t=-1
    else:
        a = Node(n1)
        b = Node(n2)
       # a.child.append(b)
        capacitymatrix[int(n1)][int(n2)] = 10000
        Nodes.append(a)
        Nodes.append(b)


print("enter the cost of each project with project number")
for i in range(n):
    c,u=input().split(" ")
    if(int(c)>0):
        capacitymatrix[0][int(u)] = int(c)
    else:
        capacitymatrix[int(u)][n+1] = -int(c)


print("lets fill our matrix")


Source = 0
Sink = len(capacitymatrix)-1
print(capacitymatrix)
G=Graph(capacitymatrix)
G.minCut(Source, Sink)
