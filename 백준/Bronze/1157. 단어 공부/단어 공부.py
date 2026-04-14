N = input().upper()
M = 0 

spell_1  = set(list(N))
spell_2  = list(N)
for cur in spell_1:
    a = spell_2.count(cur)
    if M < a:
        M = a
        ans = cur
    elif M == a:
        ans = '?'
print(ans)