S = int(input())
for _ in range(1, S+1):
    num, text = map(str, input().split())
    int_num = int(num)
    
    result = ""

    for char in text:
        result += char * int_num
    print(result)
    
