import sys
input = sys.stdin.readline

# 1. 입력 받기
size_A, size_B = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

merged_list = []
pA = pB = 0

# 2. 두 배열 비교하며 합치기 (투 포인터)
while pA < size_A and pB < size_B:
    if A[pA] < B[pB]:
        merged_list.append(A[pA])
        pA += 1
    else:
        merged_list.append(B[pB])
        pB += 1

# 3. 남은 요소들 한꺼번에 처리하기
# while문을 여러 번 쓰는 것보다 슬라이싱이 훨씬 빠르고 간결함
if pA < size_A:
    merged_list.extend(A[pA:])
if pB < size_B:
    merged_list.extend(B[pB:])

print(" ".join(map(str,merged_list)))