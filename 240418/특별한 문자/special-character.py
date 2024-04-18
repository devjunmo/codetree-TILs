input_strs = list(input())
d = dict()

for s in input_strs:
    if s in d:
        v = d[s]
        d[s] = v+1
    else:
        d[s] = 1

res = 'None'

for k, v in d.items():
    if v == 1:
        res = k
        break

print(res)