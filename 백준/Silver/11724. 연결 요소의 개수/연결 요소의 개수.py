import sys
# 재귀 깊이 제한 해제 (DFS 사용 시 필수)
sys.setrecursionlimit(10**6)

# 1. 입력 받기
input = sys.stdin.readline
N, M = map(int, input().split())

# 2. 인접 리스트로 그래프 만들기
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 기록 리스트
visited = [False] * (N + 1)

def dfs(node):
    visited[node] = True
    # 질문하신 포인트: 현재 노드의 이웃 개수만큼 반복
    # len(graph[node])를 직접 쓰지 않아도 for문이 그만큼 돌아갑니다.
    for adj in graph[node]:
        if not visited[adj]:
            dfs(adj)

# 3. 연결 요소(덩어리) 개수 세기
count = 0
for i in range(1, N + 1):
    if not visited[i]: # 방문하지 않은 새로운 정점을 발견하면
        dfs(i)         # 그 정점과 연결된 모든 정점을 방문 처리하고
        count += 1     # i 값이 false 일때 +1 을 매김

print(count)