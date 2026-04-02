#백준 25494번 a,b,c 값 대비 제일 작은 수에 맞춰 나올수 있는 x,y,z의 동일한 값의 경우의 수
roop = int(input())
for _ in range(roop):
    a,b,c = map(int,input().split())
    print(min(a, min(b,c)))