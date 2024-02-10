# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from queue import Queue

def solution(maps):
    answer = -1
    visited = set()
    current = {(0,0):1} # row, col, count
    
    len_ones = 0
    for row in maps:
        for point in row:
            if point == 1:
                len_ones += 1
    len_row = len(maps)
    len_col = len(maps[0])

    queue = Queue()
    queue.put(current)
    visited.add(list(current.keys())[0])

    while queue.empty() == False:
        
        node = queue.get()
        row_idx, col_idx = list(node.keys())[0]
        count = node[row_idx, col_idx]

        
        if row_idx == len_row-1 and col_idx==len_col-1:
            return count

        nbr_idx_set = check_nbr(maps, row_idx, col_idx, len_row, len_col, visited)

        for nbr_idx in nbr_idx_set:
            visited.add(nbr_idx)
            queue.put({nbr_idx:count+1})
    
    return answer

def check_nbr(maps, row_idx, col_idx, len_row, len_col, visited:set) -> set:
    upper_idx = (row_idx-1, col_idx)
    right_idx = (row_idx, col_idx+1)
    down_idx = (row_idx+1, col_idx)
    left_idx = (row_idx, col_idx-1)

    check_set = set()
    if not upper_idx[0] < 0:
        check_set.add(upper_idx)
    if not right_idx[1] >= len_col:
        check_set.add(right_idx)
    if not down_idx[0] >= len_row:
        check_set.add(down_idx)
    if not left_idx[1] < 0:
        check_set.add(left_idx)
    
    if check_set:
        check_set = check_set - visited

        for idx in check_set:
            if maps[idx[0]][idx[1]] == 0:
                check_set = check_set - {idx}

    return check_set



maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(solution(maps=maps))
        
