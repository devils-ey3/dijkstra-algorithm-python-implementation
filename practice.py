# def p(*x):
#     for y in x:
#         print(y)
#
#
# x =  open("graph.txt","r")
# lines = [lin.strip() for lin in x]
# it = iter(lines)
# print(list(zip(it,it,it)))
def p(*x):
    for y in x:
        print(y)

ALLVERTEXES = []
x = open('graph.txt','r')

dist = {}
prev = {}
source = "S"
target = "E"

for line in x.readlines():
    edge0,cost,edge1 = line.split()
    ALLVERTEXES.append([edge0,int(cost),edge1])
    #print(edge0,'-->',cost,'-->',edge1)
vertexies = [x for x,y,z in ALLVERTEXES] + [z for x,y,z in ALLVERTEXES]
vertexies = set(vertexies)
p(vertexies)