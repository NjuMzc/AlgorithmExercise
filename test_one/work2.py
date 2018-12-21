
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def isSorted(arr):
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
            return 0
    return 1

#每次交换后都更新查看是否有位置互换的情况,没有的话就随便找一个换一下，再看有没有互换的情况
def getMinSwapTime(arr,count):
    arr_sorted  = sorted(arr)
    for i in range(len(arr)):
        if(arr_sorted[i]==arr[i]):
            continue
        else:
            correctIndex  = arr_sorted.index(arr[i])
            nowNum = arr[correctIndex]
            if(arr_sorted.index(nowNum)==i):
                #正好互换
                count+=1
                swap(arr,correctIndex,i)
    #交换了所有互换的情况
    arr_temp = list()
    for i in range(len(arr)):
        if(arr[i]!=arr_sorted[i]):
            arr_temp.append(arr[i])
    if(len(arr_temp)==0):
        return count
    if(len(arr_temp)==2):
        count+=1
        return count
    else:
        arr_temp_sorted = sorted(arr_temp)
        correctIndex = arr_temp_sorted.index(arr_temp[0])
        swap(arr_temp,correctIndex,0)
        count+=1
        return getMinSwapTime(arr_temp,count)

def printArr(arr):
    for i in range(len(arr)):
        print(arr[i])

T = int(input())
i=0
arr_big = list()

while i<T:
    i += 1
    size = int(input())
    arr = list(map(int, input().strip().split(" ")))
    arr_big.append(getMinSwapTime(arr,0))

printArr(arr_big)