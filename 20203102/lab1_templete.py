def solution(num):
    answer = 0
    numbers = []

    while(num != 0):
        etc = num % 10
        num = num // 10
        numbers.append(etc)

    answer = sum(numbers)
    return answer

print(solution(5923)) #19
print(solution(200)) # 2
print(solution(1234567890)) #45
print(solution(2364759387)) #54
