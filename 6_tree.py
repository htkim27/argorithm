"""계층, 비선형 자료 구조
"""
from typing import Optional
from queue import Queue

class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

class TreeNode(Node)    :
    def __init__(self, data, left:Optional[Node], right:Optional[Node]):
        self.data = data
        self.left = left
        self.right = right

    # 전위 순회 : 루트 -> 왼쪽 -> 오른쪽
    # Recursive Programming
    @classmethod
    def pre_order(self, node:Optional[Node]):
        if node:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    # 중위 순회 : 왼쪽 -> 루트 -> 후위 
    @classmethod
    def in_order(self, node:Optional[Node]):
        if node:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)
    
    # 후위 순회 : 왼쪽 -> 오른쪽 -> 루트
    @classmethod
    def post_order(self, node:Optional[Node]):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=" ")


    @classmethod
    def level_order(self, root_node:Optional[Node]):
        queue = Queue()

        queue.put(root_node)

        while not queue.empty():
            node:Optional[Node] = queue.get()
            if node:
                print(node.data, end=" ")
                queue.put(node.left)
                queue.put(node.right)

    @classmethod
    def count_node(self, node:Optional[Node]):
        if node is None:
            return 0
        else:
            return 1 + self.count_node(node.left) + self.count_node(node.right)
    
    @classmethod
    def count_leaf(self, node:Optional[Node]):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return self.count_leaf(node.left) + self.count_leaf(node.right)
        
    @classmethod
    def calculate_height(self, node:Optional[Node]):
        if node is None:
            return 0
        
        h_left = self.calculate_height(node.left)
        h_right = self.calculate_height(node.right)
        if (h_left > h_right):
            return h_left + 1
        else:
            return h_right + 1

d = TreeNode("D", None, None)
e = TreeNode("E", None, None)
b = TreeNode("B", d, e)
f = TreeNode("F", None, None)
c = TreeNode("C", f, None)
root = TreeNode("A", b, c)

print("\n Pre-Order : ")
TreeNode.pre_order(root)
print("\n In-Order : ")
TreeNode.in_order(root)
print("\n Post-Order : ")
TreeNode.post_order(root)
print("\n Level-Order : ")
TreeNode.level_order(root)
print("\n Count-Node : ")
print(TreeNode.count_node(root))
print("\n Count-Leaf : ")
print(TreeNode.count_leaf(root))
print("\n Calculate-Height : ")
print(TreeNode.calculate_height(root))
print()