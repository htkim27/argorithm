"""이진 탐색 트리 : 왼쪽 자식 노드 < 부모 자식 노드 < 오른쪽 자식 노드
"""
from typing import Optional

class BinarySearchTreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left:Optional[BinarySearchTreeNode] = None
        self.right:Optional[BinarySearchTreeNode] = None

def search_bst(node:Optional[BinarySearchTreeNode], key):
    if node == None:
        return
    elif key == node.key:
        return node
    elif key < node.key:
        search_bst(node.right, key)
    elif key > node.left:
        search_bst(node.left, key)

def search_max_bst(node:Optional[BinarySearchTreeNode]):
    if node == None:
        return
    while node.right != None:
        node = node.right
    return node

def search_min_bst(node:Optional[BinarySearchTreeNode]):
    if node == None:
        return
    while node.left != None:
        node = node.left
    return node

def insert_bst(root:Optional[BinarySearchTreeNode], node:Optional[BinarySearchTreeNode]) -> bool:
    if node.key < root.key:
        if root.left == None:
            root.left = node
            return True
        else:
            return insert_bst(root.left, node)
        
    elif node.key > root.key:
        if root.right == None:
            root.right = node
            return True
        else:
            return insert_bst(root.right, node)
        
    else:
        return False # 키가 중복되면 삽입하지 않는다
    
def _delete_bst_case_1(parent:Optional[BinarySearchTreeNode], node:Optional[BinarySearchTreeNode], root:Optional[BinarySearchTreeNode]):
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None

    return root

def _delete_bst_case_2(parent:Optional[BinarySearchTreeNode], node:Optional[BinarySearchTreeNode], root:Optional[BinarySearchTreeNode]):
    if node.left == None:
        child = node.right
    else:
        child = node.left

    if node == root:
        root = child
    else:
        if node == parent.left:
            parent.left = child
        else:
            parent.right = child
    
    return root
    
def _delete_bst_case_3(parent:Optional[BinarySearchTreeNode], node:Optional[BinarySearchTreeNode], root:Optional[BinarySearchTreeNode]):
    succ_parent:Optional[BinarySearchTreeNode] = node
    succ:Optional[BinarySearchTreeNode] = node.right
    while (succ.left != None):
        succ_parent = succ
        succ = succ.left

    if (succ_parent.left == succ):
        succ_parent.left = succ.right
    else:
        succ_parent.right = succ.right

    node.key = succ.key
    node.value = succ.value

    return root

def delete_bst(root:Optional[BinarySearchTreeNode], key):
    if root == None:
        return
    
    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key :
            node = node.left
        
        