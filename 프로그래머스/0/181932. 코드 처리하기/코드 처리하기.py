def solution(code):
    ret = ""
    mode = 0
    
    # 0부터 code의 길이 - 1까지 idx를 키워가며 반복합니다.
    for idx in range(len(code)):
        if code[idx] == "1":
            # mode가 0이면 1로, 1이면 0으로 바뀜
            mode = 1 - mode
        else:
            # mode가 0일 때는 idx가 짝수일 때만 추가
            if mode == 0 and idx % 2 == 0:
                ret += code[idx]
            # mode가 1일 때는 idx가 홀수일 때만 추가
            elif mode == 1 and idx % 2 != 0:
                ret += code[idx]
    if not ret:
        return "EMPTY"
        
    return ret