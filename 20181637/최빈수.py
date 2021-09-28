def solution(lst):
    num = 0
    cnt = 0
    for i in lst:
        if lst.count(i) > cnt:
            cnt = lst.count(i)
            num = i
    answer = [i]
    return answer

print(solution([1,2,3,4,5,5])) #[5]
print(solution([12,17,19,17,23])) #[17]
print(solution([26,37,26,37,91])) #[26,37]
print(solution([28,30,32,34,144])) #[]



아직 수정 중 입니다!
