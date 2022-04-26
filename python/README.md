# 파이썬 

>문법 + 알고리즘

## 문법

### 입출력

- 데이터 입력 : `input()` 이용 - 문자열

  ```python
  # 5
  # 10 40 20 50 30 
  # 1 2 3
  n = int(input()) # 정수 1개 입력
  data = list(map(int, input().split())) # 정수 여러개 한 줄에 입력받아서 리스트로 저장
  x, y, z = map(int, input().split()) # 정수 하나씩 변수에 저장
  ```

- 시간초과 방지 데이터 입력 방법 (`input()` 은 동작 속도 느림)

  ```python
  import sys
  data = sys.stdin.readline().rstrip()
  # 또는
  input = sys.stdin.readline # 기존 input()대신 대입해서 사용
  ```

### map 함수

- `map(function, iterable)` 형태
  - 1번째 인자 : 적용시킬 함수
  - 2번째 인자 : 적용할 값들 (반복 가능한 자료형)

```python
def func_a(x):
  return x+1

list1 = list(map(int, input().split())) # 입력받은 값 각각 int 형 변환
list2 = list(map(func_a, [1, 2, 3, 4, 5])) # [2, 3, 4, 5, 6]
```

### 리스트

- 리스트 컴프리헨션 List Comprehension

  - 리스트를 초기화하는 방법 중 하나. `[조건문 + 반복문]` 형태

    ```python
    arr1 = [i for i in range(10)] # 0~9
    arr2 = [i for i in range(10) if i % 2 == 0] # 0~9 중 짝수
    arr3 = [i if i % 2 == 0 else (i+1) for i in range(1,11)] # 2, 2, 4, 4, ...
    arr4 = [[0] * m for _ in range(n)] # n x m 2차원 리스트
    ```

- 관련 메소드

  | 메소드명  | 예시                                     | 설명                                               | 시간복잡도 |
  | --------- | ---------------------------------------- | -------------------------------------------------- | ---------- |
  | append()  | list.append(1)                           | 리스트 끝에 원소 하나 삽입                         | O(1)       |
  | sort()    | list.sort()<br />list.sort(reverse=True) | 리스트 정렬. 디폴트는 오름차순 정렬                | O(NlogN)   |
  | reverse() | list.reverse()                           | 원소 순서 거꾸로                                   | O(N)       |
  | count()   | list.count(1)                            | 리스트 내 특정 원소 개수 반환                      | O(N)       |
  | insert()  | list.insert(0,1)                         | 특정 인덱스에 특정 원소 삽입                       | O(N)       |
  | remove()  | list.remove(1)                           | 특정 원소 삭제. 해당 값 여러개면 가장 앞 원소 삭제 | O(N)       |

  - len(list) : 리스트 크기 반환

### 튜플

- `(원소, 원소, ...)` 형태
- 한 번 선언된 값 변경 불가
  - 그래프 알고리즘에서 자주 사용 -> 예) 다익스트라 알고리즘 : `(비용, 노드 번호)` 형태

### 딕셔너리

- 키:값 형태. `dict()` 로 선언 가능

  - ~~순서 없음~~ 3.6부터 입력 순으로 키값 저장!
  - 해시테이블 이용 -> 리스트보다 빠른 동작 (검색/수정 : O(1))

  ```python
  dic = dict() # 딕셔너리 선언
  keyList = dic.keys() # 키 데이터 리스트
  valueList = dic.values() # 값 데이터 리스트
  ```

### 집합/셋

- `set(list)` 또는 `{원소, 원소, ...}` 형태.
  - 중복 허용하지 않음. 순서 없음.

### itertools

- product, permutations, combinations

```python
from itertools import permutations
from itertools import combinations
from itertools import product

items = ['1', '2', '3', '4', '5']
items2 = [['a', 'b', 'c,'], ['1', '2', '3', '4'], ['!', '@', '#']]

list(permutations(items, 2)) # 리스트에서 2개 뽑은 순열 (순서 다르면 다른 값)
list(combinations(items, 2)) # 리스트에서 2개 뽑은 조합 (원소 같으면 같은 값)
list(product(*items2)) # 리스트 내 리스트들에서 1개씩 뽑은 순열. 하나의 리스트 내 중복 순열도 가능
```

### collections

- deque 자료구조 : 스택과 큐의 장점을 모두 채택. 데이터 넣고 빼는 속도가 리스트형보다 빠름

```python
from collections import deque
# 큐 구현
queue = deque()
queue.append(5)
queue.append(1)
queue.popleft()
```



## 알고리즘

- 유클리드 호제법 -> 최대공약수

- 약수 구하기

- 소수 찾기 (에라토스테너스의 체)

- 해시 (+파이썬 hash 함수)

- 정규표현식

  ```python
  # 신규 아이디 추천.py 
  # 참고
  def solution(new_id):
      st = new_id
      st = st.lower()
      st = re.sub('[^a-z0-9\-_.]', '', st)
      st = re.sub('\.+', '.', st)
      st = re.sub('^[.]|[.]$', '', st)
      st = 'a' if len(st) == 0 else st[:15]
      st = re.sub('^[.]|[.]$', '', st)
      st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
      return st
  ```

- 완전탐색 : 전체 데이터 수가 100만 개 이하일 때 사용하면 적절
- DFS / BFS : 그래프 탐색 대표 알고리즘

정리 예정 ...