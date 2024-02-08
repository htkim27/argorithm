"""선입선출, 메모리공간 확보 -> 데이터처리
en_queue : 입장
de_queue : 퇴장
front : 퇴장 1순위
rear : 퇴장 마지막 순위
"""

class Queue:
    def __init__(self, size:int) -> None:
        self.size = size
        self.queue = [None for _ in range(self.size)]
        self.front = -1
        self.rear = -1

    def _is_queue_full(self):
        if self.rear == self.size-1 and self.front == -1:
            return True
        elif self.rear != self.size-1:
            return False
        else:
            for i in range(self.front):
                self.queue[i-1] = self.queue[i]
                self.queue[i]=None
            self.front -= 1
            self.rear -= 1
            return False
        
    def _is_queue_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
        
    def en_queue(self,data):
        if self._is_queue_full():
            return
        self.rear += 1
        self.queue = data

    def de_queue(self, data):
        if self._is_queue_full():
            return
        self.front += 1
        data = self.queue[data]
        self.queue[data] = None

        return data
