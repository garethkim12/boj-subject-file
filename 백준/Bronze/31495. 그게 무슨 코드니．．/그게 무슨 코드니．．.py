S = input().strip()

if len(S) >= 3 and S[0] == '"' and S[-1] == '"': #문자열이 3개 이상("A") 그리고 문자 열 이 맞는지(단어 양단에 ""있어야함)
    print(S[1:-1])
else:
    print("CE")
