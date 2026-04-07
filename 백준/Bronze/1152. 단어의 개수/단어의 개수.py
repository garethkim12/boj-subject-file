words = map(str,input().split())
count = 0
for char in words:
    if char != " ":
        count += 1
print(count)
    