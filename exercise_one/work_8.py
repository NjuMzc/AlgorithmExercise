#调整数组使差最小
#有两个序列a，b，大小都为n，序列元素的职为任意整数，无序，要求：通过交换a，b中的元素，使得序列a元素的和
#与序列b元素的和之间的差最小

#贪婪方法即可解决

m = list(map(int, input().strip().split()))
n = list(map(int, input().strip().split()))

sum_m = sum(m)
sum_n = sum(n)

diff = sum_m - sum_n  # list 总差值

while abs(diff) > 0:
    best_i, best_j = 0, 0
    best_change = 0
    for i in range(len(m)):
        for j in range(len(n)):
            change = m[i] - n[j]
            if abs(diff - 2 * change) < abs(diff - 2 * best_change):
                best_change = change
                best_i, best_j = i, j
    if best_change == 0:
        break
    m[best_i], n[best_j] = n[best_j], m[best_i]
    diff = abs(sum(m)-sum(n))
print(diff)