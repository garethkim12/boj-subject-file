#백준 2798 블랙잭
import sys
input = sys.stdin.readline

# 1. 입력 받기
N, M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0 # M에 가장 가까운 합을 저장할 변수

# 2. 3장의 카드를 뽑는 모든 경우의 수 (3중 for문)
for i in range(N): # 첫 번째 카드
    for j in range(i + 1, N): # 두 번째 카드 (첫 번째 이후부터)
        for k in range(j + 1, N): # 세 번째 카드 (두 번째 이후부터)
            
            # 세 카드의 합 계산
            total = cards[i] + cards[j] + cards[k]
            
            # 합이 M보다 작거나 같으면서, 기존 정답보다 M에 더 가깝다면 갱신
            if total <= M:
                ans = max(ans, total)

# 3. 결과 출력
print(ans)