class graph:
    def __init__(self,n_v,n_e):
        self.n=n_v
        self.m=n_e
        # self.adj_list=[[] for _ in range(n_v)]
        # self.graph=[[0 for _ in range(n_v)] for _ in range(n_v)]
        # self.res_graph=[[0 for _ in range(n_v)] for _ in range(n_v)]
        self.graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
        self.res_graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
        self.parent=[-1 for _ in range(n_v)]
        # for _ in range(n_e):
        #     a,b,c=(input()).split(' ')
        #     a,b,c=int(a),int(b),int(c)
        #     self.graph[a][b]=c
        #     self.res_graph[a][b]=c
        #     self.adj_list[a].append(b)
        # print(graph)
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
    def DFS(self,u,t):
        visited=[False for _ in range(self.n)]
        self.dfs(u,t,visited)
        # print("hell")      
        if visited[t]==True:
            return True
        return False
    def dfs(self,u,t,visited):
        visited[u]=True
        for v,_ in enumerate(self.res_graph[u]):
            if visited[v]==False and self.res_graph[u][v]>0:
                self.parent[v]=u
                return self.dfs(v,t,visited)
    def mincut(self,S,T):
        max_flow=0
        while self.BFS(S,T):
            # print("hello")
            path_flow=float("INF")
            node=T
            while node!=S:
                path_flow=min(path_flow,self.res_graph[self.parent[node]][node])
                node=self.parent[node]
            max_flow+=path_flow
            node=T
            while(node!=S):
                u=self.parent[node]
                self.res_graph[u][node]-=path_flow
                self.res_graph[node][u]+=path_flow
                node=self.parent[node]
        # print("hello")
        for i in range(self.n):
            for j in range(self.n):
                if self.res_graph[i][j] == 0 and self.graph[i][j] > 0:
                    print(str(i) + " - " + str(j))
def main():
    # print("Enter number of eges ang graphs")
    # n_v,n_e=(input()).split(' ')
    # n_v,n_e=int(n_v),int(n_e)
    g=graph(6,10)
    g.mincut(0,5)
main()