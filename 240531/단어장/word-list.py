n=int(input())
d={}
words=[
    input().strip()
    for _ in range(n)
]
words.sort()
#print(words)
for w in words:
    if w in d:
        d[w]+=1
    else:
        d[w]=1

for k,v in d.items():
    print(f'{k} {v}')