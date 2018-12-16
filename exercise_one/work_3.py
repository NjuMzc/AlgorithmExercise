#数组和窗口
#给定一个整型数组arr和一个大小为w的窗口，窗口从数组左边滑动到最右边，每次向右滑动一个位置，求出每一次滑动
#时窗口内最大元素的和

arr = list(map(int,input().strip().split(" ")))
win_size = int(input().strip())

left = 0
right = win_size-1

result = 0
while right<len(arr):
    result+=max(arr[left:right+1])
    left+=1
    right+=1
print(result)