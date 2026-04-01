from collections import deque
import sys
input = sys.stdin.readline
# 1. 입력 받기 (시간 단축을 위해 sys.stdin.readline 사용)
# N: 정점 수, M: 간선 수, R: 시작 정점
N, M, R = map(int, input().split())

# 2. 그래프 만들기 (1번부터 N번까지)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 3. 문제 조건: 인접 정점은 '오름차순'으로 방문하도록 정렬
for i in range(1, N + 1):
    graph[i].sort()

# 4. 방문 순서를 저장할 리스트와 순서 카운터
# visited[i]가 0이면 미방문, 0보다 크면 그 숫자가 방문 순서입니다.
visited = [0] * (N + 1) # 방문 기록용 방을 n+1 개 만큼 만들기 [0,0,0,0,0,0]
order = 1

def bfs(start):
    global order
    queue = deque([start])
    
    # 시작 노드 방문 처리
    visited[start] = order
    order += 1
    
    while queue:
        node = queue.popleft()
        
        # 연결된 인접 노드 확인
        for adj in graph[node]:
            # 아직 방문하지 않은 노드라면 (값이 0이라면)
            if visited[adj] == 0:
                visited[adj] = order # 현재 순서 번호표를 줍니다.
                order += 1           # 다음 번호를 위해 1 증가 graph[1] = 1, graph[2] = 2, graph[4] = 3, graph[3] = 4, graph[5] = 0 (간선이 없음) ※※※ graph[1] = [2, 4] 순번 매긴 대로 노드가 순차적으로 나감 (graph[2] = [1, 3, 4])
                queue.append(adj)    # 큐에 추가

# 5. BFS 실행
bfs(R)

# 6. 결과 출력 (1번 노드부터 N번 노드까지의 순서)
sys.stdout.write('\n'.join(map(str, visited[1:])))