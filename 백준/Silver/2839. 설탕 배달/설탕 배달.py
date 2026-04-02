N = int(input())
num_bag = 0

while True:
    if N % 5 == 0:
        num_bag += N // 5
        break

    if N < 3:
        num_bag = -1
        break

    N -= 3
    num_bag += 1

print(num_bag)