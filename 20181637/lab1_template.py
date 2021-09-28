def solution(num):
    answer = 0
    list = []
    while num // 10 != 0:
        a = num % 10
        list.append(a)
        num = num // 10
    list.append(num)
    for i in list:
        answer += i
    return answer

print(solution(5923)) #19
print(solution(200)) # 2
print(solution(1234567890)) #45
print(solution(2364759387)) #54
