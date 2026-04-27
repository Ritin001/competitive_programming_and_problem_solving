class Node:
    def __init__(self, name, price=0):
        self.name = name
        self.price = price
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def total_price(node):
    total = node.price
    for child in node.children:
        total += total_price(child)
    return total


nodes = {}

n = int(input("Enter number of items: "))

for _ in range(n):
    name, price = input("Enter name and price: ").split()
    nodes[name] = Node(name, int(price))

m = int(input("Enter number of relations (parent child): "))

for _ in range(m):
    parent, child = input().split()
    nodes[parent].add_child(nodes[child])

root_name = input("Enter root name: ")

print("Total Price:", total_price(nodes[root_name]))