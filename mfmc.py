import graph_constructor as gc
import copy
class graphs:
    def __init__(self,capacity_matrix):
        n_v=len(capacity_matrix)
        self.n=n_v
        self.fgraph=[[0 for _ in range(n_v)]for _ in range(n_v)]
        self.graph=[]
        self.res_graph=[]
        for i in range(n_v):
            self.graph.append(capacity_matrix[i][:])
            self.res_graph.append(capacity_matrix[i][:])
        # self.res_graph = [[0, 16, 13, 0, 0, 0],
        # [0, 0, 10, 12, 0, 0],
        # [0, 4, 0, 0, 14, 0],
        # [0, 0, 9, 0, 0, 20],
        # [0, 0, 0, 7, 0, 4],
        # [0, 0, 0, 0, 0, 0]]
        # print(self.graph)
        self.parent=[-1 for _ in range(n_v)]
    def BFS(self,s, t):
        visited =[False]*(self.n)
        queue=[]
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.res_graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    self.parent[ind] = u
        return True if visited[t] else False
    def mincut(self,S,T):
        max_flow=0
        while self.BFS(S,T):
            path_flow=float("INF")
            node=T
            # print(self.graph)
            while node!=S:
                path_flow=min(path_flow,self.res_graph[self.parent[node]][node])
                node=self.parent[node]
            max_flow+=path_flow
            node=T
            while(node!=S):
                u=self.parent[node]
                self.fgraph[u][node]+=path_flow
                self.res_graph[u][node]-=path_flow
                self.res_graph[node][u]+=path_flow
                node=self.parent[node]
        # for i in range(self.n):
        #     for j in range(self.n):
        #         if self.res_graph[i][j] == 0 and self.graph[i][j] > 0:
        #             print(str(i) + " - " + str(j))
def main():
    # W=[83,80,78,77]
    # R=[[0,1,6,1],[1,0,0,2],[6,0,0,0],[1,2,0,0]]
    # n=4
    lin=0
    W=[]
    R=[]
    n=0
    with open("inputforbaseball","r") as f:
        for lines in f:
            lin+=1
            if lin==1:
                n=int(lines.split()[0])
            elif lin==2:
                for i in lines.strip("\n").split():
                    W.append(int(i))
            else:
                temp=[]
                for i in lines.strip("\n").split():
                    temp.append(int(i))
                R.append(temp)
    for i in range(n):
        flag=0
        t=i
        capactiy_matrix,end=gc.construct_graph(n,W,R,t)
        g=graphs(capactiy_matrix)
        g.mincut(0,len(capactiy_matrix)-1)
        for i in range(1,end):
            if g.res_graph[0][i]!=0:
                flag=1
        if flag==1:
            print("team "+str(t)+" is eliminated")
main()
