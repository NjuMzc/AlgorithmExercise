# 最长公共子序列
# Description
# 给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。
# Input
# 输入为两行，一行一个字符串
# Output
# 输出如果有多个则分为多行，先后顺序不影响判断。
# Sample Input 1
# 1A2BD3G4H56JK
# 23EFG4I5J6K7
# Sample Output 1
# 23G456K
# 23G45JK

def LCS(s1, s2):
    stack = []  #stack[i]记录了公共子序列第i位位于s2中最前面的下标
    for c1 in s1:   # 遍历s1中每个字符
        cIndex = s2.find(c1)
        if cIndex != -1:
            i = len(stack)    # 遍历stack
            while i-1 >= 0 and cIndex < stack[i-1]:
                i -= 1
            if i == len(stack):
                stack.insert(i, cIndex)
            else:
                stack[i] = cIndex

    result = ""
    for i in stack:
        result += s2[i]
    return result


if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    print(LCS(s1, s2))







