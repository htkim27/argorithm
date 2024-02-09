

def knapsack(max_weight, num_jewels, weights, money):
    print("메모지에이션을 사용한 배낭 문제 풀이")

    array = [[0 for _ in range(max_weight+1)] for _ in range(num_jewels+1)]

    for row in range(1, num_jewels+1):
        print(f"{row}개 -> ", end=" ")
        for col in range(1, max_weight+1):
            if weights[row] > col:
                array[row][col] = array[row-1][col]
            else:
                value_1 = money[row] + array[row-1][col-weights[row]]
                value_2 = array[row-1][col]
                array[row][col] = max(value_1, value_2)

            print(f"{array[row][col]}", end=" ")

        print()

    return array[num_jewels][max_weight]


print(knapsack(7,4,[0,6,4,3,5],[0, 12]))