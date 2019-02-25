def isPrime(n):
     if n <= 1:
        return False
     j = 2
     while j*j <= n:
        if n % j == 0:
            return False
        j += 1
     return True

T = int(input())
i=0

result = list()
while(i < T):
    i+=1
    N = int(input())
    for n in range(2 , N):
        if(isPrime(n) and isPrime(N-n)):
            result.append(str(n)+" " + str((N-n)))
            break
for i, val in enumerate(result):
    print(val)