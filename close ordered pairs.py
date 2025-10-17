from random import *
from math import *

pointList=[]
for i in range(100):
    p = (randint(0,1000), randint(0,1000))
    pointList.append(p)
    print(p)

mindist = 10000
for i in range(100):
    for j in range(100):
        if (i!=j): 
            x1 = pointList[i][0]
            y1 = pointList[i][1]
            x2 = pointList[j][0]
            y2 = pointList[j][1]
            dist = sqrt((x2-x1)**2+(y2-y1)**2)
            if dist < mindist:
                mindist = dist
                p1, p2 = i, j
print(mindist,pointList[p1], pointList[p2] )
