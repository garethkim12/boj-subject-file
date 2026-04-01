import sys
sys.setrecursionlimit(10**6)
# 1. 입력 받기 (시간 단축을 위해 sys.stdin.readline 사용)
# N: 정점 수, M: 간선 수, R: 시작 정점
inp = map(int, sys.stdin.read().split())
N = next(inp)
M = next(inp)
R = next(inp)
# 2. 그래프 만들기 (1번부터 N번까지)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u = next(inp)
    v = next(inp)
    graph[u].append(v)
    graph[v].append(u)

# 3. 문제 조건: 인접 정점은 '오름차순'으로 방문하도록 정렬
for i in range(1, N + 1):
    graph[i].sort()

# 4. 방문 순서를 저장할 리스트와 순서 카운터
# visited[i]가 0이면 미방문, 0보다 크면 그 숫자가 방문 순서입니다.
visited = [0] * (N + 1) # 방문 기록용 방을 n+1 개 만큼 만들기 [0,0,0,0,0,0]
order = 1
def dfs(node):
    global order
    # [방문 처리] 현재 노드를 방문 리스트에 추가
    # 이 과정이 있어야 이미 가본 곳을 다시 가지 않습니다.
    visited[node] = order
    
    
    # [탐색] 현재 노드와 연결된 인접 노드(adj_node)를 하나씩 확인
    for adj in graph[node]:
        # 만약 인접한 노드에 아직 가본 적이 없다면 (visited_list에 없다면)
        if visited[adj] == 0:
            # [재귀 호출] 그 노드로 더 깊게 파고 들어갑니다.
            order += 1
            dfs(adj)
# 2. 1번 노드를 시작점으로 탐색 시작
dfs(R)

# 6. 결과 출력 (1번 노드부터 N번 노드까지의 순서)
sys.stdout.write('\n'.join(map(str, visited[1:])))