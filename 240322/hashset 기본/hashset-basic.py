import sys
input = sys.stdin.readline

n = int(input().strip())

s = set()

for _ in range(n):
    cmd, num = tuple(input().strip().split(' '))
    num = int(num)
    
    if cmd == 'find':
        if num in s:
            print('true')
        else:
            print('false')
    elif cmd == 'add':
        s.add(num)
    elif cmd == 'remove':
        s.remove(num)