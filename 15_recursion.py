def solution(n):
    def helper(n):
        if n <= 1:
            return 1
        return n + helper(n-1)
    answer = helper(n)
    return answer

# print(solution(10))


def solution_2(a,b):
    answer = 0

    if a==b:
        return answer
    for i in range(a+1,b+1):
        answer += i

    return answer


def solution_3(a, b):
    answer = 0
    if a>b+1:
        c=a
        a=b
        b=c

    if a==b+1:
        return answer
    else:
        return a+solution_3(a+1,b)


print(solution_3(2, 2))
print(solution_3(10, 1))
