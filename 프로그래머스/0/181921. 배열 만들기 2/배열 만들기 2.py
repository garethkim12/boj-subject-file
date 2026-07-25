def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if all(char in '05' for char in str(i)):
            answer.append(i)
    if not answer:
        return [-1]
        
    return answer