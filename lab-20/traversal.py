class node :
    def __init__(self , name):
        self.name = name
        self.left=None
        self.right=None
def pre_order(root):
    if root is None:
        return
    print(root.name)
    pre_order(root.left)
    pre_order(root.right)

m=int(input("enter the number of nodes: "))
nodes = {}
for _ in range(m):
    name, left, right = input("enter node name, left child, right child: ").split()
    if name not in nodes:
        nodes[name] = node(name)
    if left != "None":
        if left not in nodes:
            nodes[left] = node(left)
        nodes[name].left = nodes[left]
    if right != "None":
        if right not in nodes:
            nodes[right] = node(right)
        nodes[name].right = nodes[right]

root = nodes['1']
print("Pre-order Traversal:")
pre_order(root)