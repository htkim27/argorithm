"""Linked List : 메모리 공간 확보 과정 없이 데이터 처리 / current, pre를 통해 탐색
"""

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end = " ")

    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insert_node(find_data, insert_data):
    global memory, head, current, pre

    if head.data == find_data:
        node = Node()
        node.data = insert_data
        node.link = head
        head = node
        return
    
    current = head
    while current.link != None:
        pre = current
        current = current.link

        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return
    
    node = Node()
    node.data = insert_data
    current.link = node

def delete_node(delete_data):
    global memory, head, current, pre

    if head.data == delete_data:
        current == head
        head == head.link
        del(current)
        return
    
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del(current)
            return

def find_node(find_data):
    global memory, head, current, pre

    current = head
    if current.data == find_data:
        return current
    
    while current.link != None:
        current = current.link
        
        if current.data == find_data:
            return current
        
    return Node()


memory = []
head, current, pre = None, None, None
data_array = [1,2,3,4,5]

if __name__ == "__main__":
    node = Node()
    node.data = data_array[0]
    head = node
    memory.append(node)

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    print_nodes(head)

    insert_node(find_data=3, insert_data=7)
    print_nodes(head)

    delete_node(delete_data=7)
    print_nodes(head)