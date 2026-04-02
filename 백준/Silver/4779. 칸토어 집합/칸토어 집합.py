
import sys


def getContor(size):
    #base condition 
    if size == 1: return '-'
    
    # divide
    new_size = size // 3
    center = ' ' * int(new_size)
    side  = getContor(new_size)
    return side + center + side

while True:
    try:
        N = int(input())
        size = 3 ** N 
        result_str = getContor(size)
        print(result_str)
    except EOFError:
            break