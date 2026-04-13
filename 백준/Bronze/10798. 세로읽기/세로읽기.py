#백준 10798번 세로 읽기
list_A = []

# 1. 먼저 5개의 단어를 모두 입력받습니다.
for _ in range(5):
    list_A.append(input().strip())

# 2. 들여쓰기를 앞으로 당겨서, 입력이 모두 끝난 후에 세로읽기를 시작합니다.
for j in range(15): #입력 단어 값이 최대 1줄당 15개 들어와서 이렇게 작성.
    for i in range(5):
        # 3. '전체 단어 개수'가 아니라 '현재 읽고 있는 단어의 길이'와 비교합니다.
        if j < len(list_A[i]):
            print(list_A[i][j], end='')