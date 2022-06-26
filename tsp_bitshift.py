from itertools import combinations


def tsp_bitshift(graph):
    n = len(graph)
    C = [[float('inf') for _ in range(n)] for __ in range(1 << n)]
    C[1][0] = 0
    for size in range(1, n):
        for S in combinations(range(1, n), size):
            S = (0,) + S
            k = sum([1 << i for i in S])

            for i in S:
                if i == 0:
                    continue
                for j in S:
                    if j == i:
                        continue
                    cur_index = k ^ (1 << i)
                    C[k][i] = min(C[k][i], C[cur_index][j] + graph[j][i])

    all_index = (1 << n) - 1

    return min([(C[all_index][i] + graph[0][i], i) for i in range(n)])[0] # (meilen, nächstes ziel)

