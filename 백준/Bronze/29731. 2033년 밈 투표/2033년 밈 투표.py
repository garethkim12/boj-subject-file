A = int(input())
list_A = ["Never gonna give you up","Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna stop"]
list_B = []
for i in range(A):
    i = input().strip()
    if i in list_A:
        list_B.append(i)
    else:
        continue
if len(list_B) == A:
    print('No')
else:
    print('Yes')
