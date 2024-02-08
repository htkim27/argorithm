def solution(citations:list):
    answer = 0

    citations.sort(reverse=True)
    len_citations = len(citations)

    for i in range(len_citations):
        c = citations[i]
        upper_citations = citations[:i+1]
        len_upper_citations = len(upper_citations)

        if len_upper_citations >= c:
            if i > 0:
                pre_c = citations[i-1]

                if pre_c == c+1 or pre_c == c:
                    answer = c
                else:
                    for k in reversed(range(0,pre_c-c)):
                        print(k)
                        if len_upper_citations >= c+k:
                            answer = c+k
                            break
            break
    if answer == 0 and c!=0:
        for i in range(c):
            c -= 1
            len_citations >= c
            answer = c
        
    return answer


print(solution([3,0,6,1,5]))