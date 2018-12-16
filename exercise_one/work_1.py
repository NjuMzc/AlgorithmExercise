#给定数组arr和整数num，求arr的子数组中满足：其最大值减去最小值的结果小于等于num的个数。
#时间复杂度要求：O（length（arr））

#Input:输入的第一行为数组，每一个数用空格隔开，第二行为num
#Output：输出一个值




def getNnum(arr,num):
  if(len(arr)<=1):
      return 0
  min_index = 0
  max_index = 1
  if(arr[0]>arr[1]):
     min_index = 1
     max_index = 0


  left = 0
  right = 1

  res = 0
  while(right<len(arr)):
      #移动right，更新min max
      if(arr[right]<arr[min_index]):
          min_index = right
      if(arr[right]>arr[max_index]):
          max_index = right

      if(abs(arr[min_index]-arr[max_index])<=num):
          #计算满足的子数组数量
          res += 1
          right += 1
          continue
      else:
          #无法移动right
          left += 1
          if(left == right):
              right+=1
          if (arr[left] < arr[min_index]):
              min_index = left
          if (arr[left] > arr[max_index]):
              max_index = left
  return res


arr = list(map(int,input().strip().split(" ")))
num = int(input().strip())
res = getNnum(arr, num)
print(res)