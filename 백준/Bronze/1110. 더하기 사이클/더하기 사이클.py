#백준 1110번 두자리 수 더해서 원래 숫자가 나오는 사이클 횟수 찾기]
N = input() # 처음부터 문자로 받습니다.

# "2"처럼 한 자리 숫자면 앞에 "0"을 붙여서 "02"로 만들어주는 작업이 필요해요.
if len(N) == 1:
    N = "0" + N

original_N = N
count = 0

while True:
    # 1. 문자를 정수로 변환해서 더하기 (질문자님의 논리!)
    total = sum(map(int, list(N)))
    
    # 2. 새로운 숫자 조립하기
    # 원래 숫자의 맨 끝자리(N[-1]) + 더한 값의 맨 끝자리(str(total)[-1])
    new_N = N[-1] + str(total)[-1] 
    
    count += 1
    
    # 3. 사이클 확인
    if new_N == original_N:
        break
        
    N = new_N # 새로운 숫자를 다음 사이클로 넘김

print(count)