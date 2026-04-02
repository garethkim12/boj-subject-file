N,M = map(int,(input().split()))
buckets = [0] * N
for i in range(M):
    a,b,c = map(int,input().split())
    for i in range(a-1, b):
        buckets[i] = c
print(*buckets,)