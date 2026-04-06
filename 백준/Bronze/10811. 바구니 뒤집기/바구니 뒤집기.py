# 백준 10811번
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 1. 바구니 초기화: [1, 2, 3, ..., N]
bucket = [i for i in range(1, N + 1)] 

for _ in range(M):
    i, j = map(int, input().split())
    
    # 2. i번째부터 j번째까지 슬라이싱한 후 뒤집어서 다시 할당
    # 파이썬 슬라이싱 [start:end]는 end-1까지 포함하므로 j를 그대로 씁니다.
    bucket[i-1:j] = bucket[i-1:j][::-1]

# 3. 리스트 요소를 공백으로 구분하여 출력
print(*bucket)