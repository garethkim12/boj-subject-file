def fibo(num):
        if mem[num] == -1:
            mem[num] = fibo(num-1) + fibo(num-2)
        return mem[num]

n = int(input())
mem = [0, 1] + [-1] * (n-1)
print(fibo(n))