# boj 10988 펠린드롬
A  = list(input()) #단어를 쪼갠다
if A == A[::-1]:   # 쪼갠 요소를 역전해서 비교 
    print(1)       # 같을 경우 1 표시
else:         
    print(0)       #아닐 경우 0 표시
    
