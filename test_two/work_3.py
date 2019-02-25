def getind(B, A, q):
    i = 0
    while i < N:
        if B[i] < q:
            i += 1
        else:
            diff = B[i] - q

            return (A[i * 2 + 1] - diff)
    diff = q - B[N - 1]
    return (A[-1] + diff)


T = int(input())

i =0
while i<T:
    i+=1
    arr = list(map(int,input().strip().split()))

    N = arr[0]
    Q = arr[1]

    A = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]

    B = [0] * N
    B[0] = A[1] - A[0] + 1
    for i in range(1, N):
        B[i] += B[i - 1] + A[i * 2 + 1] - A[i * 2] + 1

    ind = [0] * Q
    for i in range(Q):
        ind[i] = getind(B, A, C[i])

    print(' '.join([str(x) for x in ind]))