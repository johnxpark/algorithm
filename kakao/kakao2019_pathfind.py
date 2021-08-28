import sys

sys.setrecursionlimit(10000)

class Node:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

def preorder(node: Node, res: list):
    if node is None:
        return
    res.append(node.v)
    preorder(node.left, res)
    preorder(node.right, res)

def postorder(node: Node, res: list):
    if node is None:
        return
    postorder(node.left, res)
    postorder(node.right, res)
    res.append(node.v)

def solution(nodeinfo: list):
    nodeinfo = [[node[0], node[1], i + 1] for i, node in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: x[1], reverse=True)
    print(nodeinfo)

    tree = Tree()
    tree.root = Node(*nodeinfo[0])

    for node in (nodeinfo[1:]):
        current_node = tree.root
        while True:
            if node[0] < current_node.x:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = Node(*node)
                    break
            else:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = Node(*node)
                    break

    res_preorder = []
    res_postorder = []
    preorder(tree.root, res_preorder)
    postorder(tree.root, res_postorder)

    return [res_preorder, res_postorder]

if __name__ == "__main__":
    print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
    # [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]