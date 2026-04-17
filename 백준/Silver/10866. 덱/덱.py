import sys
from collections import deque

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.read().split()
N = int(input[0])
commands = input[1:]

queue = deque()
idx = 0

for _ in range(N):
    cmd = commands[idx]
    idx += 1
    
    if cmd == "push_front":
        val = commands[idx]
        idx += 1
        queue.appendleft(val)
    elif cmd == "push_back":
        val = commands[idx]
        idx += 1
        queue.append(val)
    elif cmd == "pop_front":
        print(queue.popleft() if queue else -1)
    elif cmd == "pop_back":
        print(queue.pop() if queue else -1)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        print(0 if queue else 1)
    elif cmd == "front":
        print(queue[0] if queue else -1)
    elif cmd == "back":
        print(queue[-1] if queue else -1)