N = int(input())
result = 0

for i in range(N+1):
    A = int(i)
    B = list(str(i))
    all_plus = [int(i) for i in B]
    all_plus.append(A) 
    if sum(all_plus) == N:
        result = i
        break
print(result)