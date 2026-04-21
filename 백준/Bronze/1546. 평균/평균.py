
N = int(input())

list_a = list(map(int, input().split()))

M = max(list_a)

list_b = []
for score in list_a:
    new_score = (score / M) * 100
    list_b.append(new_score)

print(sum(list_b) / N)