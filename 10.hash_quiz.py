
CLOTHES = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    answer = 0
    clothes_dict = {}
    for i in clothes:
        if i[1] in clothes_dict:
            clothes_dict[i[1]] += 1
        else:
            clothes_dict[i[1]] = 1
    for i in clothes_dict.values():
        answer *= (i+1)
    return answer - 1