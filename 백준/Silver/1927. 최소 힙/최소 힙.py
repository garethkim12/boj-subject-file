import sys 
import heapq

input = sys.stdin.readline

my_heap = []

N = int(input())

for i in range(N):
 i = int(input())
 if i == 0:
    if len(my_heap) == 0:
      print(0)
    else:  
     print(heapq.heappop(my_heap))
 else:
   heapq.heappush(my_heap, i)