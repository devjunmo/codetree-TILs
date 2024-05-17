n = int(input().strip())
line_lst = [
    tuple(map(int, input().strip().split(' ')))
    for _ in range(n)
]

line_lst.sort()

cur_idx = 1

def is_range(c_idx, line_tup):
    x, y = line_tup
    if x <= c_idx <= y:
        return True
    else:
        return False


while cur_idx <= 1000:
    tmp_lines = []
    len_line_lst = len(line_lst)
    for i in range(len_line_lst):
        if is_range(cur_idx, line_lst[i]):
            tmp_lines.append(line_lst[i])
            line_lst.pop(i)

    cur_idx += 1