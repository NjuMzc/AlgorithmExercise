T = int(input().strip())

def perm(l):    #生成全排列
    if(len(l)<=1):
        return [l]
    r=[]
    for i in range(len(l)):
        s=l[:i]+l[i+1:]
        p=perm(s)
        for x in p:
            r.append(l[i:i+1]+x)
    return r

for i in range(T):
    Input=str(input().strip())
    numbers=[''.join(i) for i in perm(Input)]
    numbers.sort()
    output,index=False,None
    j=len(numbers)-1
    while j>=0:
        if int(numbers[j])%17==0 and numbers[j][0]!='0':
            output=True
            index=j
            break
        else:
            None
        j-=1
    if output==True:
        print(numbers[index])
    else:
        print("Not Possible")