def coordinate_compression(points, queries):
    x_coords = sorted(set(x for x, y in points) | set(x1 for x1, y1, x2, y2 in queries) | set(x2 for x1, y1, x2, y2 in queries))
    y_coords = sorted(set(y for x, y in points) | set(y1 for x1, y1, x2, y2 in queries) | set(y2 for x1, y1, x2, y2 in queries))

    x_map = {x: i + 1 for i, x in enumerate(x_coords)}
    y_map = {y: i + 1 for i, y in enumerate(y_coords)}

    compressed_points = [(x_map[x], y_map[y]) for x, y in points]
    compressed_queries = [(x_map[x1], y_map[y1], x_map[x2], y_map[y2]) for x1, y1, x2, y2 in queries]

    return compressed_points, compressed_queries, len(x_map), len(y_map)

def build_fenwick_tree(n):
    return [[0] * (n + 1) for _ in range(n + 1)]

def update(fenwick_tree, x, y, value):
    xi = x
    while xi < len(fenwick_tree):
        yi = y
        while yi < len(fenwick_tree[xi]):
            fenwick_tree[xi][yi] += value
            yi += yi & -yi
        xi += xi & -xi

def query(fenwick_tree, x, y):
    sum_value = 0
    xi = x
    while xi > 0:
        yi = y
        while yi > 0:
            sum_value += fenwick_tree[xi][yi]
            yi -= yi & -yi
        xi -= xi & -xi
    return sum_value

def query_range(fenwick_tree, x1, y1, x2, y2):
    return query(fenwick_tree, x2, y2) - query(fenwick_tree, x1 - 1, y2) - query(fenwick_tree, x2, y1 - 1) + query(fenwick_tree, x1 - 1, y1 - 1)

# 입력 받기
n, q = tuple(map(int, input().strip().split()))
points = [tuple(map(int, input().strip().split())) for _ in range(n)]
queries = [tuple(map(int, input().strip().split())) for _ in range(q)]

# 좌표 압축
compressed_points, compressed_queries, max_x, max_y = coordinate_compression(points, queries)

# 펜윅 트리 초기화
fenwick_tree = build_fenwick_tree(max(max_x, max_y))

# 점 업데이트
for x, y in compressed_points:
    update(fenwick_tree, x, y, 1)

# 질의 처리
results = []
for x1, y1, x2, y2 in compressed_queries:
    result = query_range(fenwick_tree, x1, y1, x2, y2)
    results.append(result)

# 결과 출력
for result in results:
    print(result)