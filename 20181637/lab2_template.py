def solution(lst):
    answer =[]
    dict = {}
    for i in lst:
        total = 0
        for j in lst:
            if i == j:
                total += 1
        dict[i] = total

    if len(dict.keys()) == 1:
        None
    elif max(dict.values()) == 1:
        None
    else:
        answer = [i for i, j in dict.items() if j == max(dict.values())]

    return answer

print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) # []
