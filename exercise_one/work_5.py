#区间第K最小
#找到给定数组的给定区间内的倒数第K小的数值

arr = list(map(int,input().strip().split(" ")))
start,end = list(map(int,input().strip().split()))
k = int(input().strip())
sorted_arr = sorted(arr[start-1:end])

print(sorted_arr[k-1])
