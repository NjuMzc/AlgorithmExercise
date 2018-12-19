# # 确定中间数 以中间数为基准左右删除
# num_strarr = input().split(' ')
# num_arr = []
# for i in num_strarr:
#     num_arr.append(int(i))
#
# index_arr = []
# # 先找出中间数
# for i in range(0,len(num_arr)):
#     if i == 0:
#         if num_arr[i] >= num_arr[i+1]:
#             index_arr.append(i)
#     elif i == len(num_arr) - 1:
#         if num_arr[i] >= num_arr[i-1]:
#             index_arr.append(i)
#     else:
#         if num_arr[i] >= num_arr[i+1] and num_arr[i] >= num_arr[i-1]:
#             index_arr.append(i)
#
# result_dict = []
# # 开始进行删除操作
# for i in index_arr:
#     index = num_arr[i]
#     temp_arr = num_arr.copy()
#     for j in range(len(temp_arr)-1, 0, -1):
#         if j == len(temp_arr) - 1:
#             if temp_arr[j] > index:
#                 del temp_arr[j]
#         elif j == 0:
#             if temp_arr[0] > index:
#                 del temp_arr[j]
#         elif j < i:
#             if temp_arr[j] > index or temp_arr[j] > temp_arr[j+1]:
#                 del temp_arr[j]
#         elif j > i:
#             if temp_arr[j] > index or temp_arr[j] < temp_arr[j+1]:
#                 del temp_arr[j]
#     result_dict.append(temp_arr)
#
# # 统计最长的数组
# max_num = 0
# for i in result_dict:
#     if len(i) > max_num:
#         max_num = len(i)
#
# result_str = ''
# for i in result_dict:
#     if len(i) == max_num:
#         for j in i:
#             result_str += str(j) + ' '
#         print(result_str.strip())
#     result_str = ''

def LIS(a):
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
