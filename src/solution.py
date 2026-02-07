from itertools import combinations, permutations

def hamiltonian_naive(graph, start, end):
    N = len(graph)
    n = N // 3

    vertices = list(range(N))

    others = [v for v in vertices if v != start and v != end]

    for subset_rest in combinations(others, n - 2):
        S = {start, end, *subset_rest}
        L = sorted(S)

        H = [[0] * n for _ in range(n)]
        for a in range(n):
            for b in range(n):
                H[a][b] = graph[L[a]][L[b]]

        s = L.index(start)
        t = L.index(end)

        if all_permutations(H, s, t):
            return True

    return False

def return_subgraphs(graph):
    N = len(graph)
    visited = [False] * N
    subgraphs = []
    for v in range(N):
        if not visited[v]:
            stack = [v]
            component = set()
            while stack:
                u = stack.pop()
                if not visited[u]:
                    visited[u] = True
                    component.add(u)
                    for w in range(N):
                        if graph[u][w] == 1 and not visited[w]:
                            stack.append(w)
            subgraphs.append(component)
    return subgraphs

def hamiltonian_optimized(graph, start, end):
    N = len(graph)
    n = N // 3

    subgraphs = return_subgraphs(graph)

    for component in subgraphs:
        if start in component and end in component:
            vertices = list(component)
            others = [v for v in vertices if v != start and v != end]
            for subset_rest in combinations(others, n - 2):
                S = {start, end, *subset_rest}
                L = sorted(S)

                H = [[0] * n for _ in range(n)]
                for a in range(n):
                    for b in range(n):
                        H[a][b] = graph[L[a]][L[b]]

                s = L.index(start)
                t = L.index(end)

                if all_permutations(H, s, t):
                    return True
    return False

def to_adjacency_list(graph):
    n = len(graph)
    adj = [[] for _ in range(n)]
    for u in range(n):
        for v, val in enumerate(graph[u]):
            if val != 0:
                adj[u].append(v)
    return adj

def hamiltonian_bonus(graph, start, end):
    adj_list = to_adjacency_list(graph)
    N = len(adj_list)
    target_length = N // 3
    start_subset = frozenset([start])
    dp = {(start_subset, start): True}

    for current_length in range(1, target_length):
        new_dp = {}

        for (subset, last) in dp.keys():
            for neighbor in adj_list[last]:
                if neighbor in subset:
                    continue

                new_subset_vertices = list(subset)
                new_subset_vertices.append(neighbor)
                new_subset = frozenset(new_subset_vertices)

                key = (new_subset, neighbor)
                if key not in new_dp:
                    new_dp[key] = True

        dp = new_dp

        if not dp:
            break
        
    for (subset, last) in dp.keys():
        if last == end:
            return True

    return False


def all_permutations(H, s, t):
    n = len(H)
    middle_vertices = [i for i in range(n) if i != s and i != t]

    for middle in permutations(middle_vertices):
        perm = (s,) + middle + (t,)
        if hamiltonian_check(H, perm):
            return True

    return False


def hamiltonian_check(H, perm):
    n = len(H)

    for i in range(n - 1):
        u = perm[i]
        v = perm[i + 1]
        if H[u][v] == 0:
            return False
        
    return True
