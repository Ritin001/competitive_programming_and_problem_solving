def minimax(node, depth, alpha, beta, maximizing, tree, values):
    if depth == 0 or node not in tree or len(tree[node]) == 0:
        return values.get(node, node)

    if maximizing:
        max_eval = float('-inf')
        for child in tree[node]:
            eval = minimax(child, depth - 1, alpha, beta, False, tree, values)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in tree[node]:
            eval = minimax(child, depth - 1, alpha, beta, True, tree, values)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


tree = {}
values = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = int(input("Node: "))
    children = list(map(int, input("Children: ").split()))
    tree[node] = children

l = int(input("Enter number of leaf values: "))

for _ in range(l):
    node, val = map(int, input("Leaf node and value: ").split())
    values[node] = val

root = int(input("Enter root: "))
depth = int(input("Enter depth: "))

print("Best move value:",
      minimax(root, depth, float('-inf'), float('inf'), True, tree, values))