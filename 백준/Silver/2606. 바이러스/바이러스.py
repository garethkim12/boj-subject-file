import sys

# 1. 입력 받기
num_node = int(sys.stdin.readline())
num_edge = int(sys.stdin.readline())

# 2. 그래프 만들기 (1번 노드부터 사용하므로 num_node + 1)
graph = [[] for _ in range(num_node + 1)]

for _ in range(num_edge):
    # split()을 넣어줘야 공백을 기준으로 숫자를 나눕니다.
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 기록용 리스트
visited_list = []
count = 0

# --- DFS (깊이 우선 탐색) ---
def dfs(node):
    global count
    visited_list.append(node)
    count += 1
    
    # 현재 노드와 연결된 다른 노드들을 확인
    for adj_node in graph[node]:
        if adj_node not in visited_list:
            dfs(adj_node)

# 3. 실행 및 결과 출력
dfs(1)

# 1번 컴퓨터를 제외한 '감염된' 컴퓨터 수이므로 -1
print(count - 1)