# 최대힙 : 부모 노드의 키 값이 자식노드의 키 값보다 크거나 같음

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0) # 0번 항목은 사용하지 않음

    def size(self):
        return len(self.heap)-1
    
    def is_empty(self):
        return self.size()==0
    
    def parent(self, i:int):
        return self.heap[i//2]

    def left(self, i:int):
        return self.heap[i*2]
    
    def right(self, i:int):
        return self.heap[i*2+1]
    
    def display(self, msg:str):
        print(msg, self.heap[1:])

    def insert(self, node):
        self.heap.append(node)
        i = self.size()
        while (i!=1 and node > self.parent(i)):
            self.heap[i] = self.parent(i)
            i = i//2
        self.heap[i] = node

    def delete(self): # Heap에서 delete는 루트 노드를 삭제하고 자리를 찾아주는 것
        parent = 1
        child = 2

        if not self.is_empty():
            heap_root = self.heap[1]
            last = self.heap[self.size()]

            while child <= self.size():
                if child < self.size() and self.left(parent) < self.right(parent):
                    child += 1
                if last >= self.heap[child]:
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2

            self.heap[parent] = last
            self.heap.pop(-1)
            return heap_root
        
if __name__ == "__main__":
    heap = MaxHeap()
    data = [2,5,4,8,9,3,7,3]

    print("[삽입 연산] : "+str(data))
    for elem in data:
        heap.insert(elem)

    heap.display("[삽입 후]: ")
    heap.delete()
    heap.display("[삭제 후]: ")
    heap.delete()
    heap.display("[삭제 후]: ")