# 书本分发
# -*- coding: utf-8 -*-
def check(st, page, val):
    temp = 0
    s = 1
    for i in range(len(page)):
        temp += page[i]
        if temp > val:
            temp = page[i]
            s += 1
    if s > st:
        return 1
    return 0


T = int(input())
for ss in range(T):
    book = int(input())
    pages = list(map(int, input().split()))
    st = int(input())
    hi = sum(pages)
    lo = max(pages)
    if len(pages) < st:
        print(-1)
    else:
        while lo < hi:
            mid = int((hi + lo) / 2)
            if check(st, pages, mid):
                lo = mid + 1
            else:
                hi = mid
        print(lo)
