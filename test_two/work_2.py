#磁铁问题
#
# 1/(x-a1) = 1/(a2-x)+1/(a3-x)+...+1/(an-x) a1<x < a2
T = int(input())
i = 0

while i<T:
    i+=1
    N = int(input())
    M = list(map(float,input().strip().split(" ")))

    result=""
    for j in range(len(M)-1):
        test_num = M[j]
        while test_num<M[j+1]:
            test_num += 0.001
            d1 = 0.0
            d2 = 0.0
            for k in range(0,j+1):
                d1+=1.0/(test_num-M[k])
            for k in range(j+1,len(M)):
                d2+=1.0/(M[k]-test_num)
            if(abs(d1-d2)<0.0001):
                result+=str('%.2f' % test_num)+" "
                break
    print(result.strip())