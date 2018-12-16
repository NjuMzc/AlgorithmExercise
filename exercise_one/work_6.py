#固定和的元素对
#输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字，统计这样两个数的对数

arr = list(map(int,input().strip().split()))
num = int(input().strip())
result = 0
arr_temp = [temp for temp in arr if temp <= num]

while len(arr_temp)>0:
  result += arr_temp.count(num-arr_temp[0])
  arr_temp.pop(0)
print(result)