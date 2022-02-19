# 주요 라이브러리의 문법과 유의점
파이썬의 일부 라이브러리는 잘못 사용시 수행시간이 비효율적으로 증가한다.

이를 피하는 것이 필요하다.

**표준 라이브러리**란 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리를 의미한다. 코딩테스트에서는 대부분 표준 라이브러리의 사용을 허용한다.

코딩테스트에서 꼭 알아야 하는 라이브러리는 아래의 6가지이다.
- 내장 함수: print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리
- itertools: 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리. 순열과 조합 라이브러리를 제공
- heapq: 힙(Heap) 기능을 제공하는 라이브러리. 우선순위 큐 기능을 구현하기 위해 사용
- bisect: 이진 탐색(Binary Search) 기능을 제공하는 라이브러리
- collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리
- math: 필수적인 수학적 기능을 제공하는 라이브러리. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함한다.

## 내장함수
별도의 import 명령어가 필요없는 함수들이다.


```python
# input(), print() - 데이터 입력과 출력

a = input()
print(a)
```

    Hello World
    Hello World
    


```python
# sum() - 모든 원소의 합을 반환. 리스트와 같은 iterable 객체가 입력으로 주어짐

result = sum([1, 2, 3, 4, 5])
print(result)
```

    15
    


```python
# min() - 파라미터 2개 이상이 주어질 때 가장 작은 값을 반환

result = min(7, 3, 5, 2)
print(result)
```

    2
    


```python
# max() - 가장 큰 값을 반환

result = max(7, 3, 5, 2)
print(result)
```

    7
    


```python
# eval() - 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환

result = eval("(3 + 5) * 7")
print(result)
```

    56
    


```python
# sorted() - iterable 객체가 들어왔을 때, 정렬된 결과를 반환.

result = sorted([9, 1, 8, 5, 4]) # 오름차순으로 정렬
print(result)
result = sorted([9, 1, 8, 5, 4], reverse = True) # 내림차순으로 정렬
print(result)

# 리스트의 원소로 리스트나 튜플이 존재할 때 특정한 기준에 따라서 정렬 수행 가능
# 정렬 기준은 key 속성을 이용해 명시한다.

# 2번 원소를 기준으로 내림차순 정렬
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result)
```

    [1, 4, 5, 8, 9]
    [9, 8, 5, 4, 1]
    [('이순신', 75), ('아무개', 50), ('홍길동', 35)]
    


```python
# sort() - iterable 객체는 기본으로 sort() 함수를 내장해서 굳이 sorted() 함수를 쓸 필요가 없음

data = [9, 1, 8, 5, 4]
data.sort() # 오름차순 정렬
print(data)
data.sort(reverse = True) # 내림차순 정렬
print(data)
```

    [1, 4, 5, 8, 9]
    [9, 8, 5, 4, 1]
    

## itertools
- itertools는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
- permutations(순열), combinations(조합) 클래스가 가장 유용히 쓰인다.
- permutations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산한다. 클래스이므로 객체 초기화 이후 리스트 자료형으로의 변환이 필요하다.
- combinations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다. 마찬가지로 리스트 자료형으로의 변환이 필요하다.


```python
from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)
```

    [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
    


```python
from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)
```

    [('A', 'B'), ('A', 'C'), ('B', 'C')]
    

- product는 permutations와 같은 기능을 하지만 원소의 중복을 허용한다.

- product 객체를 초기화할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다. product도 클래스이므로 객체 초기화 이후 리스트 자료형으로의 변환이 필요하다.


```python
from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)
```

    [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
    

- combinations_with_replacement는 combinations와 같은 기능을 하지만 원소의 중복을 허용한다.


```python
from itertools import combinations_with_replacement

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)
```

    [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
    

## heapq
- heapq는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용된다.
- 파이썬의 힙은 최소 힙(Min Heap)으로 구성되어 있고, 보통 최소 힙 자료구조의 최상단 원소(루트)는 항상 '가장 작은' 원소이기 때문에 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다. 
- heapq.heappush() : 힙에 원소를 삽입하는 메서드
- heapq.heappop() : 힙에서 원소를 꺼내는 메서드


```python
# 오름차순으로 힙 정렬
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    

파이썬에서는 최대 힙(Max Heap)을 제공하지 않으므로 원소의 부호를 바꾸는 방식을 사용한다.


```python
# 내림차순으로 힙 정렬
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)  # 1차로 (-) 부호 붙이기. 그럼 역으로 정렬이 됨
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h)) # 1개씩 꺼내서 담는데 부호를 붙여서 양수로 바꿈
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
```

    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    

## bisect
- 이진 탐색을 쉽게 구현할 수 있도록 하는 bisect 라이브러리가 있다.
- 정렬된 배열에서 특정한 원소를 찾을 때 효과적이다.
- bisect_left(), bisect_right() 함수가 중요하게 쓰이며, 시간복잡도는 O(logN)을 가진다.
- bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾음
- bisect_right(a, x): 정렬 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾음


```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
```

    2
    4
    

bisect_left(a, x)에 의해서 4는 [1, 2,↓ 4, 4, 8]처럼 2 뒤를 찾게 된다. (인덱스 2에 삽입하면 됨)

bisect_right(a, x)에 의해서 4는 [1, 2, 4, 4,↓ 8]처럼 8 앞을 찾게 된다. (인덱스 4에 삽입하면 됨)

이처럼 정렬된 리스트에서 효과적이며, 값이 특정 범위에 속하는 원소의 개수를 구할 때도 효과적이다.

다음은 원소의 개수를 구하는 함수를 만든 것이다.
- count_by_range(a, left_value, right_value) : 정렬된 리스트 a에서 값이 [left_value, right_valut] 범위에 있는 데이터의 개수를 반환한다. 시간 복잡도는 O(logN)이다.


```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
```

    2
    6
    

## collections
- 유용한 자료구조를 제공하는 표준 라이브러리
- deque와 Counter 클래스가 가장 유용히 쓰인다. 보통 파이썬에서는 deque를 사용해 큐를 구현한다.

### 리스트와 deque 차이
- 리스트는 append()와 pop() 메서드로 원소를 추가/삭제 할 때 가장 맨 뒤 원소를 기준으로 한다. -> 앞쪽에 있는 원소를 제거할 때 개수가 많을수록 시간이 오래 걸린다.
- deque는 리스트 자료형과 다르게 인덱싱, 슬라이싱 등의 기능은 사용 못한다. 다만, 연속적으로 나열된 데이터의 시작이나 끝부분에 데이터를 삽입/사게할 때 효과적이다.
- 시간 복잡도
 - 가장 앞쪽에 원소 추가: 리스트[O(N)], deque[O(1)]
 - 가장 뒤쪽에 원소 추가: 리스트[O(1)], deque[O(1)]
 - 가장 앞쪽의 원소 제거: 리스트[O(N)], deque[O(1)]
 - 가장 뒤쪽의 원소 제거: 리스트[O(1)], deque[O(1)]


- popleft() : 첫 번째 원소를 제거
- pop() : 마지막 원소 제거
- appendleft(x) : 첫 번째 인덱스에 원소 x 삽입
- append(x) : 마지막 인덱스에 원소 x 삽입


```python
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))  # 리스트 자료형으로 변환
```

    deque([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    

Counter는 리스트와 같은 iterable 객체에서 원소의 등장 횟수를 세는 기능을 제공한다.


```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수
print(counter['red']) # 'red'가 등장한 횟수
print(counter['green']) # 'green'이 등장한 횟수
print(dict(counter)) # 사전 자료형(dictionary datatype)으로 변환
```

    3
    2
    1
    {'red': 2, 'blue': 3, 'green': 1}
    

## math
- 자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리
- 팩토리얼, 제곱근, 최대공약수(GCD) 등을 계산해주는 기능을 포함한다.


```python
# factorial() : 팩토리얼

import math

print(math.factorial(5)) # 5 팩토리얼을 출력
```

    120
    


```python
# sqrt(x) : x의 제곱근을 반환

import math

print(math.sqrt(7))
```

    2.6457513110645907
    


```python
# gcd(a, b) : a와 b의 최대공약수를 반환

import math

print(math.gcd(21, 14))
```

    7
    


```python
# 파이(pi)와 자연상수(e)

import math

print(math.pi)  # 파이(pi) 출력
print(math.e)   # 자연상수 e 출력
```

    3.141592653589793
    2.718281828459045
    
