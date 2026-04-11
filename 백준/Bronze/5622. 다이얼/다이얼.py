#백준 5622 다이얼 걸기
# 1번 움직이는데 2초, 이후 번호 시간 정리 (2: 3초 ~ 9: 11초, 0 12초)
# 예시 : 번호에 대한 알파벳 표기: UNUCIC : 868242

# 1. 단어를 입력받습니다. (예: UNUCIC)
word_1 = input().strip()

word = word_1.upper()

# 2. 다이얼 정보를 리스트로 묶어서 만듭니다.
# 인덱스 0번부터 각 알파벳 뭉치들을 넣어둡니다.
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

total_time = 0

# 3. 입력받은 단어에서 한 글자씩 꺼냅니다.
for char in word:
    # 4. dial 리스트를 돌면서 해당 글자가 어디에 있는지 찾습니다.
    for i in range(len(dial)):
        if char in dial[i]:
            # 다이얼 2번(ABC)은 3초가 걸립니다. 
            # 리스트 인덱스 i가 0일 때 3초이므로, i + 3을 더해줍니다.
            total_time += (i + 3)

print(total_time)