# 백준 3009번 문제 이상함 (x,y) 좌표 행렬 중에 1개만 있는 것 출력
list_A = []
list_B = []
for _ in range(3):
    a, b = map(int,input().split())
    list_A.append(a)
    list_B.append(b)

for i in list_A:
    if list_A.count(i) == 1:
        answer_A = i

for i in list_B:
    if list_B.count(i) == 1:
        answer_B = i

print(answer_A, answer_B)