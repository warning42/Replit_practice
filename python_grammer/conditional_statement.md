# 조건문
- 프로그램을 작성할 때 프로그램의 흐름을 제어하는 문법


```python
# 20 이상일 때만 출력하도록 설정

x = 15

print(x)

if x > 20:
    print(x)
else:
    print('x는 20 미만입니다.')
```

    15
    x는 20 미만입니다.
    


```python
# if ~ elif ~ else 문 
x = 13

if x < 10:
    print('x는 10 미만입니다.')
elif 10 <= x < 20:
    print('x는 10 이상 20 미만입니다.')
else:
    print('x는 20 이상입니다.')

print('판단을 종료합니다.')
```

    x는 10 이상 20 미만입니다.
    판단을 종료합니다.
    

파이썬에서는 들여쓰기를 스페이스바 4번 입력하여 작성한다.

탭 사용자와 스페이스바 4번 입력하는 사용자, 둘로 나뉘는데 이왕이면 스페이스바 4번 입력하는 것에 익숙해지도록 하는 것이 좋다고 저자는 말했다.

if ~ elif ~ else 문을 벗어난 print()는 그대로 실행됨에 주의하자.

### 비교 연산자
- x == y : x와 y가 같을 때 True, 다르면 False
- x != y : x와 y가 다를 때 True, 다르면 False
- x > y  : x가 y보다 클 때 True, 작으면 False
- x < y  : x가 y보다 작을 때 True, 크면 False
- x >= y : x가 y보다 크거나 같을 때 True, 작으면 False
- x <= y : x가 y보다 작거나 같을 때 True, 작으면 False

### 논리 연산자
파이썬에는 총 3가지 논리 연산자가 있다.
- x and y : x와 y가 모두 참(True)일 때 참(True)이다.
- x or y  : x와 y 중에 하나만 참(True)이어도 참(True)이다.
- not x   : x가 거짓(False)일 때 참(True)이다.

### 파이썬의 기타 연산자
파이썬은 추가적으로 'in 연산자'와 'not in 연산자'를 제공한다. iterable 자료형에서 사용된다.
- X in 리스트 : 리스트 안에 X가 들어가 있을 때 참(True)이다.
- X not in 문자열 : 문자열 안에 X가 들어가 있을 때 참(True)이다.

if 조건문을 사용할 때 아무런 행동을 하지 않게 하려면 pass를 입력하면 된다.


```python
score = 85

if score >= 80:
    pass # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')
```

    프로그램을 종료합니다.
    

조건부 표현식(conditional expression)을 이용하면 if ~ else 문을 한 줄에 작성할 수 있다.


```python
score = 85
result = "Success" if score >= 80 else "Fail"
print(result)
```

    Success
    

조건부 표현식은 리스트 생성이나, 리스트 원소 제거에도 유용히 쓰인다.


```python
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)
```

    [1, 2, 4]
    

다음처럼 더 간단하게 적을 수도 있다.


```python
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]

print(result)
```

    [1, 2, 4]
    
