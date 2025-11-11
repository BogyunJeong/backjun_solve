def solution(clothes):
    answer = 1

    dict = {}
    lst = []

    for c,t in clothes:
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1
    for cnt in dict.values():
        answer *= (cnt + 1)

    return answer - 1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])