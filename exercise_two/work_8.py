# 非递归合并排序
# Description
# 合并（归并）排序的核心思想是：每次从中间位置将数组分组再分别排序。请实现其非递归方案。
# Input
# 输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。
# Output
# 输出的每一行为排序结果，用空格隔开，末尾不要空格。
# Sample Input 1
# 13 24 3 56 34 3 78 12 29 49 84 51 9 100
# Sample Output 1
# 3 3 9 12 24 29 34 49 51 56 78 84 100
def mergeSort(nums):
    stack = []  # 待排序的子数组栈
    for num in nums:    # 初始化栈
        stack.append([num])

    while len(stack) != 1:
        length = len(stack)
        tempStack = []  # 临时栈
        for i in range(0, length, 2):
            nums1 = stack.pop()
            nums2 = stack.pop() if stack else None
            tempStack.append(merge(nums1, nums2))

        stack = tempStack

    return stack[0]

def merge(nums1, nums2):
    length1 = len(nums1) if nums1 else 0
    length2 = len(nums2) if nums2 else 0
    i = 0   # 遍历nums1的指针
    j = 0   # 遍历nums2的指针
    result = []
    while i < length1 and j < length2:
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    if i < length1:
        result += nums1[i:]
    if j < length2:
        result += nums2[j:]
    return result

if __name__ == '__main__':
    while 1:
        try:
            nums = [int(num) for num in input().strip().split(' ') if num][1:]
            if nums:
                print(" ".join([str(num) for num in mergeSort(nums)]))
        except EOFError:
            break