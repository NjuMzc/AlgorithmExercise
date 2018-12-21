def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def printArr(arr):
    for i in range(len(arr)):
        print(arr[i])

def getStrArr(arr):
    s = ""
    for i in range(len(arr)):
        s+= str(arr[i])
        if(i<len(arr)-1):
            s+=" "
    return  s

T = int(input())
i=0
arr_big = list()

while i<T:
    i += 1
    size_list = list(map(int, input().strip().split(" ")))
    arr_1 = list(map(int, input().strip().split(" ")))
    arr_2 = list(map(int, input().strip().split(" ")))
    arr_temp = list()
    for j in range(len(arr_1)):
        if(arr_2.count(arr_1[j])==0):
            arr_temp.append(arr_1[j])
    arr_temp = sorted(arr_temp)
    for j in range(len(arr_temp)):
        arr_1.remove(arr_temp[j])
    for j in range(len(arr_1)):
        for k in range(0, len(arr_1) - 1 - j):
            if(arr_2.index(arr_1[k])>arr_2.index(arr_1[k+1])):
                    swap(arr_1, k, k + 1)
    arr_big.append(getStrArr(arr_1)+" "+getStrArr(arr_temp))
printArr(arr_big)
