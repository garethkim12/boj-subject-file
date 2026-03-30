#boj 5073 삼각형과 세 변
while True:
    # 1. str이 아니라 int로 받아서 숫자 비교가 가능하게 합니다.
    A, B, C = map(int, input().split())
    
    # 종료 조건: 세 수가 모두 0일 때
    if A == 0 and B == 0 and C == 0:
        break
    
    sides = sorted([A, B, C]) # [가장작은값, 중간값, 가장큰값] 순서로 정렬됨
    
    if sides[2] >= sides[0] + sides[1]:
        print('Invalid')
    
    # 3. 삼각형 종류 판별 (성립 조건 통과 후 실행)
    elif A == B == C:
        print('Equilateral')
    elif A == B or B == C or A == C:
        print('Isosceles')
    else:
        print('Scalene')