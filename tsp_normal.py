import itertools

#https://gist.github.com/vyraun/4faab4a3ab50c43a290bc1b216ce8853


def tsp_normal(graph):
    A = {(frozenset([0, index + 1]), index + 1): (dist, [0, index + 1]) for index, dist in enumerate(graph[0][1:])}
    cnt = len(graph)
    for m in range(2, cnt):
        B = {}

        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min([(A[(S-{j}, k)][0] + graph[k][j], A[(S-{j}, k)][1] + [j]) for k in S if k != 0 and k != j])
        A = B

    res = min([(A[d][0] + graph[0][d[1]], A[d][1]) for d in iter(A)])
    return res[0]
