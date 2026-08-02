from collections import Counter

def solution(a, b, c, d):
    counts = Counter([a, b, c, d])
    if len(counts) == 1:
        p = list(counts.keys())[0]
        return 1111 * p

    elif len(counts) == 2:

        items = counts.most_common()
        p, count_p = items[0]
        q, count_q = items[1]        

        if count_p == 3:
            return (10 * p + q) ** 2

        else:
            return (p + q) * abs(p - q)


    elif len(counts) == 3:
        items = counts.most_common()

        q = items[1][0]
        r = items[2][0]
        return q * r

    else:
        return min(a, b, c, d)