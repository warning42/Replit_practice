# 큰수의 법칙
"""동빈이의 큰 수의 법칙
다양한 수로 이루어진 배열이 있을 때
주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 특징"""

# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어짐

N, M, K = map(int, input().split())

num = list(map(int,input().split()))

sum = 0

num.sort()

if M == 0:
    sum = 0
else:
    while M > 0:
        for _ in range(0,K):
            if M == 0:
                break
            sum += num[-1]
            M = M - 1
        if M == 0:
            break
        sum += num[-2]
        M = M - 1

print(sum)