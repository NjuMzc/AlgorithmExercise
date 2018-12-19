#固定和的元素对
#输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字，统计这样两个数的对数

num_strarr = input().split(' ')
num_arr = []
for i in num_strarr:
    num_arr.append(int(i))
sum = int(input())
count = 0
for i in range(len(num_arr) - 1):
    for j in range(i+1, len(num_arr)):
        if num_arr[i] + num_arr[j] == sum:
            count += 1

print(count)