from itertools import permutations

def tsp_brute_force(graph):
    n = len(graph)
    all_cities = set(range(n))
    min_cost = float('inf')
    best_path = None

    for path in permutations(range(1, n)):
        current_cost = 0
        current_path = [0] + list(path) + [0]

        for i in range(n - 1):
            current_cost += graph[current_path[i]][current_path[i + 1]]

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return best_path, min_cost

# Example Usage
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_path, min_cost = tsp_brute_force(graph)
print("Best Path:", best_path)
print("Minimum Cost:", min_cost)
