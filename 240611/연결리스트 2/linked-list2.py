class Node:
    def __init__(self, node_numb):
        self.node_numb = node_numb
        self.prev = None
        self.next = None
        

n = int(input())
q = int(input())

node_lst = [0]
for i in range(1,n+1):
    node_lst.append(Node(i))


def pop_node(node):
    pass

def insert_node_front(i):
    pass

def insert_node_back(i):
    pass

for i in range(q):
    query = tuple(map(int, input().strip().split(' ')))
    i = query[1]
    j = 0
    if query[0] == 1:
        node = node_lst[i]
        pop_node(node)
    elif query[0] == 2:
        j = query[2]
    elif query[0] == 3:
        j = query[2]
    elif query[0] == 4:
        pass