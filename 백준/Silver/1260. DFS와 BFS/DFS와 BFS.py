from collections import deque
import sys

# 1. 입력 받기 (N: 노드 수, M: 간선 수, V: 시작 노드)
N, M, V = map(int, sys.stdin.readline().split())

# 2. 그래프 만들기 (1번 노드부터 사용하므로 N+1)
graph = [[] for _ in range(N + 1)]

for _ in range(M): # 간선의 개수 M만큼 반복해야 함
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 기록용 리스트
visited_list = []

# --- DFS (깊이 우선 탐색) ---
def dfs(node):
    visited_list.append(node)
    print(node, end=' ')
    
    # 작은 번호부터 방문하기 위해 정렬
    for adj_node in sorted(graph[node]):
        if adj_node not in visited_list:
            dfs(adj_node)

# --- BFS (너비 우선 탐색) ---
def bfs(start):
    queue = deque([start])
    visited_list.append(start)
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        
        for adj_node in sorted(graph[node]):
            if adj_node not in visited_list:
                visited_list.append(adj_node)
                queue.append(adj_node)

# 3. 결과 출력
dfs(V)
print() # 줄바꿈

visited_list.clear() # 방문 기록 초기화

bfs(V) # 두 번째는 BFS를 호출해야 함