N, M = map(int,input().split())
basket = [ i for i in range(1, N+1)] 
for _ in range(M):
 i, j = map(int,input().split())
 real_i = i - 1
 real_j = j - 1
 basket[real_i], basket[real_j] = basket[real_j], basket[real_i] 
print(*basket) 