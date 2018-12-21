
def printArr(arr):
    for i in range(len(arr)):
        print(arr[i])

def getRevertNum(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                count+=1
    return count
T = int(input())
i=0
arr_big = list()

while i<T:
    i += 1
    size = int(input())
    arr = list(map(float, input().strip().split(" ")))
    arr_big.append(getRevertNum(arr))

printArr(arr_big)

#下面是归并排序的做法
def merge_sort(li, count):
    if len(li) == 1:
        return li
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    ll = merge_sort(left, count)
    rl = merge_sort(right, count)

    return merge(ll, rl, count)


# 这里接收两个列表
def merge(left, right, count):
    # 从两个有顺序的列表里边依次取数据比较后放入result
    # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result

    result = []
    while len(left) > 0 and len(right) > 0:
        # 为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            count[0] += len(left)
            result.append(right.pop(0))
    # while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    result += left
    result += right
    return result


test_case = int(input())
for i in range(0, test_case):
    input_length = int(input())
    num_arr = list(map(int, input().strip().split(' ')))
    count = [0]
    merge_sort(num_arr,count)
    print(count[0])