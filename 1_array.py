""" Array : 메모리 공간 확보 -> 데이터 처리"""

class Array:
    def __init__(self, array:list):
        self.array = array

    def add_data(self, data):
        self.array.append(None)
        len_array = len(self.array)
        self.array[len_array-1] = data

    def insert_data(self, data, position):
        self.array.append(None)
        len_array = len(self.array)

        for i in range(len_array-1, position, -1):
            self.array[i] = self.array[i-1]
            self.array[i-1] = None

        self.array[position] = data

        return self.array

    def delete_data(self, position):
        self.array[position] = None
        len_array = len(self.array)

        for i in range(position,len_array-1):
            self.array[i] = self.array[i+1]
            self.array[i+1] = None
            
        del self.array[len_array-1]

        return self.array
    
array = Array([1,2,3,4,5])
print(array.delete_data(position=1))
