def solution(genres, plays):
    g_i_dict = {}
    i_p_dict = {}
    g_ps_dict = {}

    i=0
    for g, p in zip(genres, plays):
        if g not in g_i_dict:
            g_i_dict[g] = [i]
        else:
            g_i_dict[g].append(i)

        if g not in g_ps_dict:
            g_ps_dict[g] = p
        else:
            g_ps_dict[g] += p

        i_p_dict[i] = p

        i+=1
    
    g_ps_items_desc = sorted(g_ps_dict.items(), key=lambda item: item[1], reverse=True)

    answer = []
    for g, _ in g_ps_items_desc:

        i_list = []
        for i in g_i_dict[g]:
            i_list.append(i)
        i_list.sort()

        i_p_items = []
        for i in i_list:
            i_p_items.append([i,i_p_dict[i]])
        
        i_p_items_desc = sorted(i_p_items, key=lambda item: item[1], reverse=True)

        if len(i_p_items_desc) >= 2:
            answer.append(i_p_items_desc[0][0])
            answer.append(i_p_items_desc[1][0])

        else:
            answer.append(i_p_items_desc[0][0])





    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500,600,150,800,2500]

print(solution(genres=genres, plays=plays))