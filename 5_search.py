# 순차 탐색

def seq_search(array:list, find_data):
    position = -1
    size = len(array)

    for i in range(size):
        if array[i] == find_data:
            position = i
            break

    return position

array = [188,150,168,105,120,177,50]
find_data = 0
print(seq_search(array, find_data))
find_data = 120
print(seq_search(array, find_data))


# 이분 탐색 : sorted 되어 있을 때
def bin_search(array:list, find_data):
    position = -1
    start = 0
    end = len(array)-1

    while start <= end:
        mid = (start + end) // 2
        mid_data = array[mid]
        if find_data == mid_data:
            position = mid
            break
        elif find_data > mid_data:
            start = mid+1
        elif find_data < mid_data:
            end = mid-1

    return position

array = [188,150,168,105,120,177,50]
find_data = 0
print(bin_search(array, find_data))
find_data = 120
print(bin_search(array, find_data))