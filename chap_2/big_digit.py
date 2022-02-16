# 큰수의 법칙
"""동빈이의 큰 수의 법칙
다양한 수로 이루어진 배열이 있을 때
주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 특징"""

# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어짐

from random import randint

N = randint(2, 1000)
while True:
  M = randint(1, 10000)
  K = randint(1, 10000)
  if K <= M:
    break
  else:
    continue

A = []
for _ in range(0,N):
  A.append(randint(1, 10000))

print(N, M, K, sep=',', end=' ')
print(A, sep=' ')

