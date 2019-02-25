import math
class Point:
    x =0
    y =0
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getManhattan(self,pointB):
        return float(abs(pointB.x - self.x) + abs(pointB.y - self.y))
    def getEuclidean(self,pointB):
        return math.sqrt(pow((pointB.x - self.x),2)+ pow((pointB.y - self.y),2))
    def isEqual(self,pointB):
        return self.getManhattan(pointB)==self.getEuclidean(pointB)

T = int(input())
i = 0
result = list()

while(i<T):
    i+=1
    N = int(input())
    pointArr = list()
    count = 0
    for j in range(0,N):
        x,y = input().strip().split(" ")
        pointArr.append(Point(int(x),int(y)))
    for j in range(len(pointArr)-1):
        p = pointArr[j]
        for k in range(j+1,len(pointArr)):
            if(p.isEqual(pointArr[k])):
                count+=1
    result.append(count)

for i, val in enumerate(result):
    print(val)
