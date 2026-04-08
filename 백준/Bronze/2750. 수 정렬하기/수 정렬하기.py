N = int(input())
total = []
for i in range(N):
    data_int = int(input())
    total.append(data_int)
total.sort()

print(*total)