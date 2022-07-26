# Today I Learned

# 데이터 구조

mutable vs. immutable  →  내용 수정 가능 여부 <br/>

- mutable : 리스트, 셋, 딕셔너리
- immutable : 튜플, 레인지, bool, int, float, str


데이터 구조 활용 => 메서드 (method) 활용
- 메서드 : 클래스 내부에 정의한 함수 (즉, 객체의 기능)
- 함수(모든 자료형) vs. 메서드(특정 자료형)
- **데이터 구조.메서드()**  -->> ex) list.append(10)
<br/><br/>

# 순서가 있는 데이터 구조
## 1. 문자열
- 문자들의 나열
- 모든 문자는 str 타입 (변경 불가능한 **immutable**)

``` python
word = 'ssafy'
print(word) # ssafy
print(id(word))  # 메모리 주소 확인 2114201356016

word = 'test'
print(word)  # test
print(id(word))  # 메모리 주소 확인 2114201357872

# 실제로 파이썬 변수 안에는 주소만 들어감
```
<br/>

## 문자열 조회 / 탐색 / 검증 메서드


  | <center>문법</center> |                   설명                    |
  | :-------------------: | :---------------------------------------: |
  |       s.find(x)       | x의 첫 번째 위치를 반환. 없으면 -1을 반환 |
  |      s.index(x)       | x의 첫 번째 위치를 반환. 없으면 오류 발생 |
  |      s.isalpha()      |   알파벳 문자 여부 (유니코드 상 Letter)   |
  |      s.isupper()      |                대문자 여부                |
  |      s.islower()      |                소문자 여부                |
  |      s.istitle()      |             타이틀 형식 여부              |
<br/>

  - .find(x)
    ``` python
    print('apple'.find('p'))  # 1
    print('apple'.find('k'))  # -1
    ```

  - .index(x)
    ``` python
    print('apple'.index('k'))  # 오류
    ```
  - 문자열 관련 검증 메서드
    ``` python
    print('abc'.isalpha())   # True
    print('ㄱㄴㄷ'.isalpha())   # True
    print('Ab'.isupper())  # False
    print('ab'.islower())   # True
    print('Title Title'.istitle())  # True
    ```
    <img width="450" src= https://i.esdrop.com/d/f/GQtKpTuAPv/LZyNurlfQa.png alt="문자열 검증 메서드">
    --> 아직 잘 이해하지 못했음

<br/><br/>

## 문자열 변경 메서드

  |     <center>문법</center>      |                                     설명                                      |
  | :----------------------------: | :---------------------------------------------------------------------------: |
  |  s.replace(old, new[,count])   |                  바꿀 대상 글자를 새로운 글자로 바꿔서 반환                   |
  |        s.strip([chars])        |                           공백이나 특정 문자를 제거                           |
  | s.split(sep=None, maxsplit=-1) |                      공백이나 특정 문자를 기준으로 분리                       |
  |  'separator'.join([iterable])  |                           구분자로 iterable을 합침                            |
  |         s.capitalize()         |                       가장 첫 번째 글자를 대문자로 변경                       |
  |           s.title()            | 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자, 나머지는 소문자로 변환 |
  |           s.upper()            |                              모두 대문자로 변경                               |
  |           s.lower()            |                              모두 소문자로 변경                               |
  |          s.swapcase()          |                            대 <-> 소문자 서로 변경                            |

<br/><br/>

> 문자열은 **immutale**인데, 문자열 변경이 되는 이유는?
>> 기존의 문자열을 변경하는 게 아니라, 변경된 문자열을 새롭게 만들어서 반환

<br/>

``` python
a = [3, 1, 2]
a.sort()
print(a)  # [1, 2, 3]
>> 리스트 - mutable

b = “hello”
b.replace(“h”, “j”)
print(b)  # hello
>> str - immutable
``` 


<br/>

- 문자열 변경


  - **.replace(old, new[,count])**
    - count를 지정하면, 해당 개수만큼만 시행 


  - **.strip([chars])**
    - 문자열을 지정하지 않으면 공백 제거
    - 양쪽 제거(strip) / 왼쪽 제거(lstrip) / 오른쪽 제거(rstrip)


  - **.split(sep=None, maxsplit=-1)**
    - 문자열을 특정한 단위로 나눠 리스트로 반환
    - sep=None 또는 지정 X -> 연속 공백문자를 단일로 간주, 선/후행 공백은 빈 문자열에 포함 X
    - maxsplit = -1 : 제한없음
    ``` python
    print('a,b,c'.split(','))  # ['a', 'b', 'c']
    print('a b c'.split())  # ['a', 'b', 'c']
    ```

  - 'separator'.join([iterable])
    - iterable에 문자열이 아닌 값이 있으면 TypeError 발생
    ``` python
    print('*'.join('ssafy'))  # s*s*a*f*y
    print(' '.join(['3', '5']))  # 3 5
    ```
<br/>

- 문자열 변경 예시
  ``` python
  msg = 'hi! Everyone, I\'m ssafy'
  print(msg.capitalize())  # Hi! everyone, i'm ssafy
  print(msg.title())  # Hi! Everyone, I'M Ssafy
  print(msg.upper())  # HI! EVERYONE, I'M SSAFY
  print(msg.lower())  # hi! everyone, i'm ssafy
  print(msg.swapcase())  # HI! eVERYONE, i'M SSAFY
  ```
<br/><br/>

---
<br/>

## 2. 리스트 
- 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
- **가변 자료형**
- 인덱스를 통해 접근 가능
<br/><br/>

## 리스트 메서드

  | <center>문법</center>  |                             설명                              |
  | :--------------------: | :-----------------------------------------------------------: |
  |      L.append(x)       |               리스트 마지막에 항목 x를 **추가**               |
  |     L.insert(i, x)     |                리스트 인덱스 i에 항목 x를 삽입                |
  |      L.remove(x)       |     리스트 첫 번째 항목 x를 제거 (존재 X 시, ValueError)      |
  |        L.pop()         |               리스트 마지막 항목을 반환 후 제거               |
  |        L.pop(i)        |          리스트 인덱스 i에 있는 항목을 반환 후 제거           |
  |      L.extend(m)       |        순회형 m의 모든 항목들의 리스트 끝에 추가 (+=)         |
  | L.index(x, start, end) | 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환 |
  |      L.reverse()       |                      리스트 거꾸로 정렬                       |
  |        L.sort()        |                          리스트 정렬                          |
  |       L.count(x)       |        리스트에서 항목 x가 몇 개 존재하는지 갯수 반환         |
<br/>

- 값 추가 및 삭제


  - .append(x)

  ``` python
  cafe = ['starbucks', 'tomntoms', 'hollys']
  print(cafe)  # ['starbucks', 'tomntoms', 'hollys']
  print(cafe, id(cafe))  # 2394792166528

  cafe.append('banapresso')
  print(cafe)  # ['starbucks', 'tomntoms', 'hollys', 'banapresso']
  print(cafe, id(cafe))  # 2394792166528

  # 주소값 같음
  ```

  - .insert(i, x)
    - 정해진 위치 i에 x값 추가
    - 리스트 길이보다 큰 경우 맨 뒤에 추가

  ``` python
  cafe.insert(0, 'start')
  print(cafe)  # ['start', 'starbucks', 'tomntoms', 'hollys', 'banapresso']

  cafe.insert(10000, 'end')
  print(cafe)  # ['start', 'starbucks', 'tomntoms', 'hollys', 'banapresso', 'end']
  ```

  - .extend(iterable)
  ``` python
  cafe.extend(['coffee'])
  print(cafe)  # ['start', 'starbucks', 'tomntoms', 'hollys', 'banapresso', 'end', 'coffee']

  cafe.extend('cup')
  print(cafe)  # ['start', 'starbucks', 'tomntoms', 'hollys', 'banapresso', 'end', 'coffee', 'c', 'u', 'p']

  # 문자열로 추가됨
  ```

  - .remove(x) : 값이 x인 것 삭제


  - .pop(i) : i 위치에 있는 값을 삭제 + 반환
    - i가 지정되지 않으면 => 마지막 항목

  - .clear() : 모든 항목 삭제

<br/>

- 탐색 및 정렬


  - .index(x)
    - 없는 경우 ValueError


  - .count(x) : 값이 x인 것의 개수

  - **.sort()** -- 원본 리스트를 정렬. None 반환
  - **sorted** -- 원본은 그대로 두고, 새로운 리스트를 만듦

  ``` python
  numbers = [3, 2, 5, 7]
  result = numbers.sort()
  print(numbers, result)  # [2, 3, 5, 7] None

  numbers = [3, 2, 6, 8]
  result = sorted(numbers)
  print(numbers, result)  # [3, 2, 6, 8] [2, 3, 6, 8]
  ```

  - .reserve() : 정렬X
<br/><br/>

--- 

## 3. 튜플
- 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
- **불변 자료형**
- 리스트 메서드 중 항목을 변경하는 메서드들을 제외하고 대부분 동일
<br/>
``` python
a = (1, 2, 3, 5, 1)
a[0] = 5
# 'tuple' object does not support item assignment
```
<br/>

#### 멤버십 연산자
- 포함 여부 확인
  - in
  - not in
- 산술연산자 (+) : 시퀀스 간의 concatenation(연결/연쇄)
- 반복연산자 (*)




---

<br/><br/>

# 순서가 없는 데이터 구조

## 1. 셋
- 중복되는 요소가 없이, 순서가 상관없는 데이터들의 묶음
- 집합 연산 가능
- **가변 변수형**

| <center>문법</center> |                                    설명                                    |
| :-------------------: | :------------------------------------------------------------------------: |
|       s.copy()        |                        셋의 **얕은 복사본**을 반환                         |
|       s.add(x)        |                          항목x가 셋에 없다면 추가                          |
|        s.pop()        |               랜덤하게 항목 반환 후 제거 (빈 셋 -> KeyError)               |
|      s.remove(s)      |                  항목 x 삭제 (항목 존재x 시 -> KeyError)                   |
|     s.discard(x)      |                       항목 x가 셋에 있는 경우, 삭제                        |
|      s.update(t)      |               셋 t에 있는 모든 항목 중 셋 s에 없는 항목 추가               |
|       s.clear()       |                               모든 항목 제거                               |
|    s.isdisjoint(t)    | 셋 s가 셋 t의 서로 같은 항목을 하나라도 갖지 않은 경우, True 반환 (서로소) |
|     s.issubset(t)     |                  셋 s가 셋 t의 하위 셋인 경우, True 반환                   |
|    s.issuperset(t)    |                  셋 s가 셋 t의 상위 셋인 경우, True 반환                   |
<br/>


<img width="300" src= https://i.esdrop.com/d/f/GQtKpTuAPv/WDDD0AhcH8.png alt="집합">

<br/>

- 추가 및 변경
  - .add()
  - .update() : 여러 값을 추가

- 삭제
  - .remove()  --> 없으면 KeyError
  - .discard()  --> 없어도 에러 발생 X
  - .pop()
  - .clear() : 모든 항목 제거

- 집합 관련 함수
  - s.isdisjoint(t) : 서로소 
  - s.issubset(t) : 하위 셋
  - s.issuperset(t) : 상위 셋

  ``` python
  a = {'사과', '바나나', '수박'}
  b = {'포도', '망고'}
  c = {'사과', '포도', '망고', '수박', '바나나'}

  print(a.isdisjoint(b))  # a와 b가 서로소인가? True
  print(a.isdisjoint(c))  # a와 c가 서로소인가? False
  print(a.issubset(c))  # a가 c의 하위 셋인가? True
  print(b.issubset(c))  # b가 c의 하위 셋인가? True
  print(c.issuperset(a))  # c가 a의 상위 셋인가? True
  print(c.issuperset(b))  # c가 b의 상위 셋인가? True
  print(b.issubset(a))  # b가 a의 하위 셋인가? False
  ```
<br/><br/>

--- 

## 2. 딕셔너리
- 키-값 쌍으로 이루어진 자료형
- 키 = immutable 데이터만 활용 가능


<br/>


| <center>문법</center> |                    설명                     |
| :-------------------: | :-----------------------------------------: |
|       d.clear()       |              모든 항목을 제거               |
|       d.copy()        |              얕은 복사본 반환               |
|       d.keys()        |      딕셔너리의 모든 키를 담은 뷰 반환      |
|      d.values()       |      딕셔너리의 모든 값을 담은 뷰 반환      |
|       d.items()       |   딕셔너리의 모든 키-값 쌍을 담은 뷰 반환   |
|       d.get(k)        |       키 k의 값 반환 (없을 경우 None)       |
|      d.get(k, v)      |      키 k의 값 반환 (없을 경우 v 반환)      |
|       d.pop(k)        | 키 k의 값 반환 후 삭제 (없을 경우 KeyError) |
|      d.pop(k, v)      |  키 k의 값 반환 후 삭제 (없을 경우 v 반환)  |
|   d.update([other])   |      딕셔너리의 값을 매핑하여 업데이트      |
<br/>


- 조회
  - .get(key[,default])
    - key를 통해 value를 가져옴
    - KeyError 발생 X
    - default 값 설정 O (기본 : None)

    ``` python
    my_dict = {'apple': '사과', 'banana': '바나나'}
    print(my_dict.get('pineapple'))  # None
    print(my_dict.get('apple'))  # 사과
    print(my_dict.get('pineapple', 0))  # 0
    ```

    ```python
    my_dict = {'apple': '사과', 'banana': '바나나'}

    for value in my_dict.values():
        print(value)  
    # 사과
    # 바나나

    for key, value in my_dict.items():
        print(f'key : {key} / value : {value}')
    # key : apple / value : 사과   
    # key : banana / value : 바나나
    ```

- 추가 및 삭제
  - .pop(key[,default])
    - key가 딕셔너리에 있으면 제거하고 해당 값 반환
    - 없으면 default 반환 (default 값이 없으면 KeyError)

    ``` python
    my_dict = {'apple': '사과', 'banana': '바나나'}
    data = my_dict.pop('apple')
    print(data, my_dict)  # 사과 {'banana' : '바나나'}

    data = my_dict.pop('apple', 0)
    print(data)  # 0
    ```

  - .update() : 덮어쓰기
