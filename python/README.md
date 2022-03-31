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

  

### 리스트

- 리스트 컴프리헨션 List Comprehension

  - 리스트를 초기화하는 방법 중 하나. `[조건문 + 반복문]` 형태

    ```python
    arr1 = [i for i in range(10)] # 0~9
    arr2 = [i for i in range(10) if i % 2 == 0] # 0~9 중 짝수
    arr3 = [[0] * m for _ in range(n)] # n x m 2차원 리스트
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

  - 순서 없음
  - 해시테이블 이용 -> 리스트보다 빠른 동작 (검색/수정 : O(1))

  ```python
  dic = dict() # 딕셔너리 선언
  keyList = dic.keys() # 키 데이터 리스트
  valueList = dic.values() # 값 데이터 리스트
  ```

### 집합/셋

- `set(list)` 또는 `{원소, 원소, ...}` 형태.
  - 중복 허용하지 않음. 순서 없음.

### 