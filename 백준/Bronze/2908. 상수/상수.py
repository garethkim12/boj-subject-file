# 백준 2908 상수 (숫자자리 바꾼 후 큰 값 표출)
math = [int(i[::-1]) for i in input().split()] # 리스트 안에서 값을 한 번 받을 때 수를 반전하여 리스트에 담기 

print(max(math)) # 들어 있는 값 중에 최댓 값 출력