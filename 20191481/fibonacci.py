import time
import random

# 피보나치 재귀함수 사용
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

# 피보나치 반복적
def iterfibo(n):
    if n == 0:
        return 0
    else :
        a = 0
        b = 1
        for i in range(1, n):
            a, b = b, a + b
    return b

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo_recur(%d)=%d, time %.6f" %(nbr, fibonumber, ts)) # 피보나치_재귀 결과, 경과시간
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("Fibo_iter(%d)=%d, time %.6f" %(nbr, fibonumber, ts)) # 피보나치_반복 결과, 경과시간
