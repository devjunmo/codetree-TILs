import heapq

n = int(input())
pq = []

for _ in range(n):
    cmds = input().strip().split(' ')
    cmd = cmds[0]
    if cmd == 'push':
        v = cmds[1]
        heapq.heappush(pq, v)
    elif cmd == 'pop':
        pv = heapq.heappop(pq)
        print(pv)
    elif cmd == 'size':
        print(len(pq))
    elif cmd =='empty':
        if not pq:
            print(1)
        else:
            print(0)
    elif cmd =='top':
        print(pq[0])