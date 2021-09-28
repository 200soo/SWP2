def solution(num):
    answer = 0
    while num // 10 != 0:
        a = num % 10
        answer += a
        num = num // 10
    answer += num
    return answer

print(solution(5923)) #19
print(solution(200)) # 2
print(solution(1234567890)) #45
print(solution(2364759387)) #54
