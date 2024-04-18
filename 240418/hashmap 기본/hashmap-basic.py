n = int(input())

cmds = [
    (input().strip().split(' '))
    for _ in range(n)
]

d = dict()

for cmd in cmds:
    if cmd[0] == 'add':
        k = cmd[1]
        v = cmd[2]
        d[k] = v
    elif cmd[0] == 'remove':
        k = cmd[1]
        if k in d:
            d.pop(k)
    elif cmd[0] == 'find':
        k = cmd[1]
        if k in d:
            print(d[k])
        else:
            print('None')