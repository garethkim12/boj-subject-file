#boj 2581번 소수
import sys

# 1. 입력 받기
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

list_primes = []

# 2. M부터 N까지 하나씩 소수인지 확인
for i in range(M, N + 1):
    if i < 2:  # 1은 소수가 아니므로 제외
        continue
    
    is_prime = True  # 일단 소수라고 가정
    
    
    for j in range(2, int(i**0.5) + 1): # 2부터 해당 숫자의 제곱근까지만 나누어 봐도 소수 판별이 가능
        if i % j == 0:     # 나누어떨어지는 수가 있다면
            is_prime = False # 소수가 아님
            break          # 더 이상 검사할 필요 없음
            
    if is_prime: # 끝까지 살아남은(True) 숫자만 리스트에 추가
        list_primes.append(i)

# 3. 결과 출력
if not list_primes:  # 리스트가 비어있다면 (소수가 없다면)
    print(-1)
else:
    print(sum(list_primes))
    print(min(list_primes))