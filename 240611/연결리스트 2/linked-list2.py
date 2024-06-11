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
    if node.prev is not None:
        node.prev.next=node.next
    if node.next is not None:
        node.next.prev=node.prev
    
    node.prev=None
    node.next=None


def insert_node_front(node, i):
    tgt_node=node_lst[i]
    node.prev=tgt_node.prev
    node.next=tgt_node

    if tgt_node.prev is not None:
        tgt_node.prev.next=node
    tgt_node.prev=node
    

def insert_node_back(node, i):
    tgt_node=node_lst[i]
    node.prev=tgt_node
    node.next=tgt_node.next

    if tgt_node.next is not None:
        tgt_node.next.prev=node
    tgt_node.next=node


for i in range(q):
    query = tuple(map(int, input().strip().split(' ')))
    i = query[1]
    j = 0
    if query[0] == 1:
        node = node_lst[i]
        pop_node(node)
    elif query[0] == 2:
        j = query[2]
        insert_node_front(node_lst[j],i)
    elif query[0] == 3:
        j = query[2]
        insert_node_back(node_lst[j],i)
    elif query[0] == 4:
        v1,v2=0,0
        n1=node_lst[i].prev
        n2=node_lst[i].next
        if n1 is not None:
            v1=n1.node_numb
        if n2 is not None:
            v2=n2.node_numb
        print(f'{v1} {v2}')

res=[]
for i in range(1,n+1):
    if node_lst[i].next is not None:
        res.append(node_lst[i].next.node_numb)
    else:
        res.append(0)

print(*res)