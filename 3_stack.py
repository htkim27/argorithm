"""선입후출, 메모리공간확보 -> 데이터처리
push: 스택에 데이터를 쌓음,
pop: 맨 위 데이터를 꺼내옴
"""
class Stack:
    def __init__(self, size:int):
        self.size = size
        self.stack = [None for _ in range(size)]
        self.top = -1

    def _is_stack_full(self):
        if self.top >= self.size-1:
            return True
        else
            return False
        
    def _is_stack_empty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def push(self, data):

        if self._is_stack_full():
            return
        self.top += 1
        self.stack[self.top] = data

        return data
    
    def pop(self, data):

        if self._is_stack_empty():
            return
        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1

        return data
    
    def peek(self):
        if self._is_stack_empty():
            return
        else:
            return self.stack[self.top]