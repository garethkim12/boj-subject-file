#백준 15829번 해쉬 문제

M = 1234567891
r = 31

L = int(input())
A = input().lower().strip()

hesh = 0

for i in range(L):

# a:1, b:2, .... ord(A[i]) - ord('a') + 1
# a 값 * r ** i
    hesh +=   (ord(A[i]) - ord('a') + 1) * r ** i

print(hesh % M)