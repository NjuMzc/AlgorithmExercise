#求汉诺塔的移动次数
#f(n) = 2 + 3*f(n-1)

n = int(input().strip())
result = 0
for i in range(0,n):
    result = result*3 + 2
print(result)