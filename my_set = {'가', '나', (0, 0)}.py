def ordered_difference_sets(set1, set2):
    diff1 = set1 - set2 
    diff2 = set2 - set1
    if diff1 > diff2:
        return diff2,diff1
    elif diff1 ==diff2:
        return diff2,diff1
    else: 
        return diff1,diff2
    

# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})
