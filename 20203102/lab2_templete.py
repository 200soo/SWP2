def solution(lst):
    answer = []
    #리스트 내용 확인
    #리스트에 있는 숫자 중복 확인
    #중복 숫자가 가장 큰 값 리턴
    count = [0] * max(lst)

    for num in lst:
        count[num-1] = count[num-1] + 1

    if max(count) == 1:
        return answer
    else:
        number = 0
        for i in count:
            number += 1
            if i == max(count):
                answer.append(number)

    return answer

print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]
