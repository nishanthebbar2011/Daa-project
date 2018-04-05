def construct_graph(n,W,R,t):
    # print("Enter the number of teams")
    # n=5
    # print("enter number of games won by each team")
    # W=[0,0,0,0,0]
    # print("numbre of mathes remaining btw R and W")
    # R=[[0,4,4,4,4],[4,0,4,4,4],[4,4,0,4,4],[4,4,4,0,4],[4,4,4,4,0]]
    #number of game nodes is number matches in the upper triangular matrix

    # print("enter the team number you want to test ranges from 0 to n-1")
    # t=2
    remainingfort=0
    for i in range(n):
        remainingfort+=R[t][i]

    #creating the graph matrix
    total=2+((n-1)*n)//2
    capacitymatrix=[[0 for i in range(total+1)]for i in range(total+1)]
    #index
    source=0
    destination=total
    gamesstart=1
    gamesend=((n-2)*(n-1))//2
    teamstart=gamesend+1
    teamend=total-1
    #print(gamesend-gamesstart," ",gamesstart," ",gamesend," ",total)
    #matrix init
    #count goes from gamestart to gamesend
    count=gamesstart
    for i in range(n):
        for j in range((i+1),n):
            if (i!=t) and (j!=t):
                capacitymatrix[0][count]=R[i][j]
                capacitymatrix[count][teamstart+i]=float("INF")
                capacitymatrix[count][teamstart+j]=float("INF")
                capacitymatrix[teamstart+i][total]=W[t]+remainingfort-W[i]
                capacitymatrix[teamstart+j][total]=W[t]+remainingfort-W[j]
                count=count+1
    # for i in range(total+1):
    #     for j in range(total+1):
    #         print(capacitymatrix[i][j]," ",end="")
    #     print()
    return capacitymatrix,gamesend
# W=[0,0,0,0,0]
# R=[[0,4,4,4,4],[4,0,4,4,4],[4,4,0,4,4],[4,4,4,0,4],[4,4,4,4,0]]
# cm=construct_graph(5,W,R,2)
# print(cm)
