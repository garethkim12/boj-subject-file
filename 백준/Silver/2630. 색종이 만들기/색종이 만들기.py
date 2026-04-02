N = int(input()) # 종이의 한 변의 길이 (2, 4, 8, 16, 32, 64, 128 중 하나)
paper = []       # 전체 종이의 색상 정보를 담을 2차원 리스트
color_list = []  # 잘라진 색종이들의 색상을 저장할 리스트

# 종이 데이터 입력받기
for _ in range(N):
    # 각 행(row)을 리스트로 변환하여 paper에 추가 (2차원 배열 완성)
    paper.append(list(map(int, input().split())))

def makePaper(row, col, size):
    # 1. 현재 영역의 첫 번째 칸 색상을 기준으로 잡음
    color = paper[row][col] 
    
    # 2. 현재 설정된 영역(size x size)을 돌며 모두 같은 색인지 확인
    for i in range(row, row + size):
        for j in range(col, col + size):
            # 기준 색상과 다른 색이 하나라도 발견되면?
            if paper[i][j] != color:
                # 3. 영역을 4등분하기 위해 사이즈를 절반으로 줄임
                new_size = size // 2
                
                # 4. 4개의 구역(1사분면, 2사분면, 3사분면, 4사분면)에 대해 다시 함수 호출
                # 좌측 상단
                makePaper(row, col, new_size)
                # 우측 상단
                makePaper(row, col + new_size, new_size)
                # 좌측 하단
                makePaper(row + new_size, col, new_size)
                # 우측 하단
                makePaper(row + new_size, col + new_size, new_size)
                
                # 더 이상 현재 함수를 진행하지 않고 종료 (재귀 탈출)
                return

    # 5. 모든 칸이 같은 색이라면 해당 색상을 결과 리스트에 저장
    color_list.append(color)

# 시작점(0,0)부터 전체 크기(N)만큼 함수 실행
makePaper(0, 0, N) 

# 결과 출력: 0(하얀색)의 개수와 1(파란색)의 개수를 각각 카운트
print(color_list.count(0))
print(color_list.count(1))