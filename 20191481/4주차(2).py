def solution(list):
    answer = []
    cnt = [0] * max(list)

    for i in list:
        cnt[i-1] = cnt[i-1] + 1

    if max(cnt) == 1:
        return answer
    else:
        num = 0
        for j in cnt:
            num += 1
            if j == max(cnt):
                answer.append(num)

    return answer


print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]
