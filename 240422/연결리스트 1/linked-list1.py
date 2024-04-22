class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# 1 S_value
def push_front(S_value, cur):
    new_node = Node(S_value)

    # 새로 만든 노드의 prev는 cur의 prev에, next는 cur에 연결
    new_node.prev = cur.prev
    new_node.next = cur

    # 연결한 new node 기준 조작
    ## prev에 새로 달린 노드 후처리
    if new_node.prev is not None:
        # 원래 이 노드의 next는 cur였으니까 new node로 바꿔주기
        new_node.prev.next = new_node
    
    ## next에 새로 달린 노드 후처리
    if new_node.next is not None:
        # 원래 이 노드의 prev는 cur_prev였으니까 new node로 바꿔주기
        new_node.next.prev = new_node



# 2 S_value
def push_back(S_value, cur):
    new_node = Node(S_value)

    # 새로 만든 노드의 prev, next에 필요한 노드 연결
    new_node.prev = cur
    new_node.next = cur.next

    # new node에 새로 연결된 노드에 대한 후처리
    if new_node.prev is not None:
        new_node.prev.next = new_node
    if new_node.next is not None:
        new_node.next.prev = new_node


# 3
def change_to_back():
    global cur
    if cur.prev is not None:
        cur = cur.prev


# 4
def change_to_front():
    global cur
    if cur.next is not None:
        cur = cur.next




# cur의 이전 노드의 값, 노드 cur의 값, 노드 cur의 다음 노드의 값을 차례대로 한 줄에 출력
# 존재하지 않는다면, 그 노드의 값 대신에 (Null)을 출력
def print_node(cur):
    pd = '(Null)'
    nd = '(Null)'
    
    if cur.prev is not None:
        pd = cur.prev.data
    
    if cur.next is not None:
        nd = cur.next.data
    
    res = [pd, cur.data, nd]
    print(*res)


S_init = input()
cur = Node(S_init)

n = int(input())

for _ in range(n):
    cmds = input().strip().split(' ')
    if cmds[0] == '1':
        S_value = cmds[1]
        push_front(S_value, cur)

    elif cmds[0] == '2':
        S_value = cmds[1]
        push_back(S_value, cur)

    elif cmds[0] == '3':
        change_to_back()

    elif cmds[0] == '4':
        change_to_front()
    
    print_node(cur)