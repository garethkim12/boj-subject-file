def solution(my_string, overwrite_string, s):
    answer = ''
    A1 = my_string[:s]
    A2 = my_string[s + len(overwrite_string):]
    answer =  A1 + overwrite_string + A2
    return answer