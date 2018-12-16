#先升后降
#从一列数中筛除尽可能少的数使得从左往右看，这些数是从小到大再从大到小的


#先将数组划分为升序或者降序的排列
def LIS(a):
    '''
    求最长子序列，返回 长度，子序列
    '''
    a = list(a)
    length = len(a)
    num = [1] * length  # DP中记录每个位置为末尾的最大LIS长度
    pos = [0] * length  # 记录位置
    for i in range(length):
        for j in range(i):
            if a[j] < a[i] and num[i] < num[j] + 1:
                num[i] = num[j] + 1
                pos[i] = j

    length_max = max(num)
    index_max = num.index(length_max)

    lis = []
    lis.append(a[index_max])
    for i in range(length_max - 1):
        lis.append(a[pos[index_max]])
        index_max = pos[index_max]
    # print(lis)
    lis.reverse()
    return length_max, lis


def print_res(m):
    # 按照题目要求格式输出一行
    s = ''
    m = list(m)
    for i in range(len(m)):
        s += str(m[i])
        s += ' '
    print(s.strip())
    return


arr = list(map(int, input().strip().split()))

max_i = []  # 分界点（arr[i]包含在m,n中）
len_res = []  # 最大长度
ms = []
ns = []

for i in range(len(arr)):
    length_m, m = LIS(arr[:i + 1])
    temp = arr[i:len(arr)]
    temp.reverse()
    length_n, n = LIS(temp)
    len_res.append(length_m + length_n - 1)
    ms.append(m)
    ns.append(n)

len_max = max(len_res)
for i in range(len(len_res)):
    if len_res[i] == len_max:
        m = ms[i]
        n = ns[i]
        n.reverse()
        if m[-1] == n[0]:
            m.extend(n[1:])
        else:
            m.extend(n)
        print_res(m)

