n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  n %= coin

print(count)

"""for 문을 확인하면 동전 크기에 상관없이
    동전 종류만 시간 복잡도에 관련있음을 알 수 있다.
    시간 복잡도 -> O(K)   K:동전 종류
"""