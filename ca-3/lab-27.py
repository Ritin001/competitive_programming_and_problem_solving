class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1


def min_new_friendships(n, edges):
    dsu = DSU(n)
    for u, v in edges:
        dsu.union(u, v)

    components = len(set(dsu.find(i) for i in range(n)))
    return components - 1


n = int(input("Enter number of people: "))
e = int(input("Enter number of friendships: "))

edges = []
for _ in range(e):
    u, v = map(int, input().split())
    edges.append((u, v))

print("Minimum new friendships:", min_new_friendships(n, edges))