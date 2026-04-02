# 1. 행렬의 크기 N(세로), M(가로) 입력받기
n, m = map(int, input().split())

# 2. 첫 번째 행렬(A) 입력받아 저장하기
matrix_a = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix_a.append(row)

# 3. 두 번째 행렬(B) 입력받아 저장하기
matrix_b = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix_b.append(row)

# 4. 두 행렬을 더하면서 바로 출력하기
for i in range(n):
    for j in range(m):
        # 같은 위치의 원소를 더함
        result = matrix_a[i][j] + matrix_b[i][j]
        print(result, end=" ")
    print() # 한 줄 출력이 끝나면 줄바꿈