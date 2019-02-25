# 杀人
T = int(input())

i = 0

while i<T:
    i+=1
    P = int(input())
    count = 0
    while P > 0:
        count+=1
        P = P - count*count
        if(P<0):
            count-=1
    print(count)
