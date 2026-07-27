def solution(arr, queries):
    answer = [] 
    for s, e, k in queries:
        filtered = [arr[i] for i in range(s, e + 1) if arr[i] > k]
        if filtered:
            answer.append(min(filtered))
        else:
            answer.append(-1)
    return answer