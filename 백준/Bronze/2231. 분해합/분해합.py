# 백준 2231 분해 합 (각 자리 수를 낱개로 추가 더하는 값 표출)
N = int(input())
# 반복문을 찾을 때 조건에 맞는 최종 값을 담을 변수 만들기
result = 0

# 1부터 N 까지 조건을 반복
for i in range(1, N+1):
    # 원 숫자의 정수와 100, 10, 1의 자리 를 각각 변수로 만들기 (자리수에 대한 데이터는 문자로 인식 후 분해)
    A = int(i)
    B = list(str(i))
    # 리스트에 문자로 만든 자릿수를 정수로 바꿔서 리스트에 넣기 (1, 2, 3)
    all_plus = [int(i) for i in B]
    # 이후 원 숫자의 정수 값을 넣기(123)
    all_plus.append(A) 

    #조건식: 순차적으로 다 더해서 N 이랑 값이 동일해 지는 값이면 종료 후 최종 값을 담아서 표시
    if sum(all_plus) == N:
        result = i
        break
print(result)