def check_connection(pc1,pc2):
    pc_list = {}
    x = open('pcToRouter.txt', 'r')
    for line in x.readlines():
        pc_list[line.split()[0]] = line.split()[1]
    if pc1 not in pc_list.keys():
        print(pc1,"is not connected there")
        exit(0)
    if pc2 not in pc_list.keys():
        print(pc2,"is not connected there")
        exit(0)
    return pc_list[pc1],pc_list[pc2]

def dijsker(sOurce,tArget):
    ALLVERTEXES = []
    x = open('graph.txt1','r')
    source = sOurce
    target = tArget
    path = []
    for line in x.readlines():
        edge0,cost,edge1 = line.split()
        ALLVERTEXES.append([edge0,int(cost),edge1])

    vertexies = set([x for x,y,z in ALLVERTEXES] + [z for x,y,z in ALLVERTEXES])
    BIGNUMBER = 99
    UNDEFINED = "null"

    Q = vertexies
    u = ""
    dist = {}
    prev = {}

    for v in vertexies:
        dist[v] = BIGNUMBER
        prev[v] = UNDEFINED
    dist[source] = 0

    while len(Q)!=0:
        minimum_distance = BIGNUMBER + 1
        for x in Q:
            if dist[x] < minimum_distance:
                u = x
                minimum_distance = dist[x]
        Q.remove(u)


        for (a,w,v) in ALLVERTEXES:
            if a == u:
                alt = dist[u] + w
                if alt < dist[v]:
                    dist[v]=alt
                    prev[v]=u

        if u == target:
            #u = target
            while prev[u] != UNDEFINED:
                path.append(u)
                u = prev[u]
            total_cost = dist[target]
            for path in path+[source][::-1]:
                print(path,end=' -> ')
            print("Cost : ",total_cost)


if __name__=="__main__":
    userInput = input("Enter the where you send data pc1 to pc2 : ").lower().split()
    x = check_connection(userInput[0],userInput[1])
    dijsker(x[0],x[1])
    #dijsker()