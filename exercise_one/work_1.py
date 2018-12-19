#给定数组arr和整数num，求arr的子数组中满足：其最大值减去最小值的结果小于等于num的个数。
#时间复杂度要求：O（length（arr））

#Input:输入的第一行为数组，每一个数用空格隔开，第二行为num
#Output：输出一个值
arr = list(map(int, input().strip().split(' ')))
n = int(input())
result_arr = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr) + 1):
        result_arr.append(arr[i:j])
count = 0
for i in result_arr:
    if max(i) - min(i) > n:
        count += 1
print(count)