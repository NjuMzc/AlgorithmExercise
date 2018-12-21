def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def printArr(arr):
    s = ""
    for i in range(len(arr)):
        s+= str(arr[i])
        if(i<len(arr)-1):
            s+=" "
    print(s)


T = int(input())
i=0
arr_big = list()

while i<T:
   i+=1
   size = int(input())
   arr = list(map(int,input().strip().split(" ")))

   arr_counter=list()
   arr_num = list()
   for j in range(len(arr)):
      if(arr_num.count(arr[j])==0):
          arr_num.append(arr[j])
          arr_counter.append(1)
      else:
          index = arr_num.index(arr[j])
          arr_counter[index] += 1
   #排序arr_counter
   for j in range(len(arr_num)):
       for k in range(0,len(arr_num)-1-j):
           if(arr_counter[k]<arr_counter[k+1]):
               swap(arr_counter,k,k+1)
               swap(arr_num,k,k+1)
   #对同样数量的按照从小到大排序
   for j in range(len(arr_num)):
       for k in range(0,len(arr_num)-1-j):
           if(arr_counter[k]==arr_counter[k+1]):
               if(arr_num[k]>arr_num[k+1]):
                   swap(arr_num, k, k + 1)
   #输出结果
   arr_result = list()
   for j in range(len(arr_num)):
       for k in range(arr_counter[j]):
           arr_result.append(arr_num[j])
   arr_big.append(arr_result)

for i in range(len(arr_big)):
    printArr(arr_big[i])



