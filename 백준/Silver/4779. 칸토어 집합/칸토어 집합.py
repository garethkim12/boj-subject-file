
import sys


def getContor(size):
    #base condition 
    if size == 1: return '-'
    
    # divide
    new_size = size // 3
    center = ' ' * int(new_size)
    side  = getContor(new_size)
    return side + center + side

total = sys.stdin.read().split()
for line in total:
    N = int(line)
    size = 3 ** N
    result_str = getContor(size)
    print(result_str)
