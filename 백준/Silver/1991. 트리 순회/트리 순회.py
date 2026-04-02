# 백준 1991번 트리순회 (나중에 손코딩 함)
# binary tree traversal (boj 1991번)

num_node = int(input())

tree = {}

# 1. 트리 생성 (딕셔너리 활용)
for _ in range(num_node):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

# 2. 전위 순회 (Root -> Left -> Right)
def preorder(node):
    if node == '.':
        return
    print(node, end='')       # Root
    preorder(tree[node][0])   # Left
    preorder(tree[node][1])   # Right

# 3. 중위 순회 (Left -> Root -> Right)
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])    # Left
    print(node, end='')       # Root
    inorder(tree[node][1])    # Right

# 4. 후위 순회 (Left -> Right -> Root)
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])  # Left
    postorder(tree[node][1])  # Right
    print(node, end='')       # Root

# 실행 및 출력
preorder('A')
print()
inorder('A')
print()
postorder('A')