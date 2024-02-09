def solution(N, number):
    answer = 0
    
    if N == number:
        answer = 1
        return answer        
    
    memory = {1:{N}}
    for i in range(1,9):
        num_list = memory[i]
        if number in num_list:
            answer = i
            break
        
        add_nums = set()
        add_nums.add(int(f"{N}"*(i+1)))

        if i == 1:
            add_nums.add(N+N)
            add_nums.add(N-N)
            add_nums.add(N*N)
            add_nums.add(N//N)
        else:
            for j in range(1,i):
                # memory[j] + memory[i-j]
                for k in memory[j]:
                    for n in memory[i+1-j]:
                        print("?", j, i-j)
                        add_nums.add(n+k)
                        add_nums.add(n-k)
                        add_nums.add(n*k)
                        if k!=0:
                            add_nums.add(n//k)

                        print(add_nums)


        memory[i+1] = add_nums


        # print(f"[{i+1}] : ",memory[i+1])

    if answer == 0:
        answer = -1
        return answer 

    return answer

N=5
number=12

print(solution(N, number))