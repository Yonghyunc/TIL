# 문자열 (string)


## 코드체계 
- 과거 : 지역 별로 코드 체계 다름
- 네트워크 발전으로 서로 정보를 주고 받을 때 문제가 생김 <br/>
--> 표준안 ASCII 코드

<br/><br/>


### "비트" 개념을 통해 컴퓨터에서 문자 표현
- 컴퓨터가 표현할 수 있는 가장 작은 단위 (0, 1)
- 1 바이트 = 8 비트 (2^8의 문자 표현이 가능)
- 문자열 --> 바이트로 표현


<br/><br/>

### ASCII 
- 128개 표현 가능(7비트 인코딩) -- 첫 번째 비트는 오류검사용 (케이트 비트?)
- 알파벳을 표현하는 데 목적 (미국 기준)

### 다국어 처리 ==> 유니코드 

ASCII와 유니코드의 문자는 컴퓨터에서 그림으로 저장되고, 비트로 ....


<br/>

#### 유니코드 인코딩

- UTF-8 : 8비트 단위로 인코딩 / 가변길이 방식 -> 공간적으로 효율적 / ASCII 코드와 호환이 좋음
- UTF-16, UTF-32 - 공간 고정적

<br/><br/>

---

## python에서 문자열 처리 <br/>
: 컨테이너 / 시퀀스 / 변경 x / iterable

1. indexing, slicing
2. 메서드
+ ord, chr

<br/><br/>

--- 

# 문자열 슬라이싱
> 문자열은 iterable
문자열[start:end:step]
- start : 범위 시작 인덱스 (포함)
- end : 범위 끝 인덱스 (포함X)
- step : 간격 (음수는 반대 방향)

``` python
word = "abcdefghi"

word[2:5]
>> cde

word[-6:-2]
>> defg

# 양수, 음수 인덱스 혼합 가능
word[2:-4]
>> cde

# step
word[2:5:2]
>> ce

# step : 음수는 반대 방향 의미
word[5:2:-1]
>> fed

# start, end, step 지정하지 않으면 기본값으로
word[:3]
>> abc

word[5:]
>> fghi

word[:]
>> abcdefghi

word[::-1]
>> ihgfedcba

# 범위를 넘어가는 슬라이싱은 빈 문자열 반환
word[10:20]
>> 
```

<br/><br/>

# 문자열 메서드 
❗ 파이썬의 문자열은 immutable <br/>
즉, 문자열 메서드는 원본 문자열 수정 ❌ <br/>
단순히 메서드를 적용한 형태의 리스트를 새로 반환

<br/>

## .split(기준 문자)
- 문자열을 일정 기준으로 나눠 리스트로 반환
- 기본값 : 공백

``` python
# 입력 받을 때 많이 사용
num = input().split()
```

<br/>

## .strip(제거할 문자)
- 문자열의 **왼/오른쪽**에서 특정 문자 제거
- 기본값 : 공백

``` python
word = "abcd adea"

print(word.strip('a'))

>> bcd ade

# 가운데의 문자는 제거하지 않음
```

<br/>

## .find(찾는 문자)
- 특정 문자가 처음으로 나타나는 위치(인덱스) 반환
- 찾는 문자가 없다면 **-1** 반환

``` python
word = "apple"

print(word.find("p"))
>> 1

print(word.find("K"))
>> -1
```

<br/>

## .index(찾는 문자)
- 특정 문자가 처음으로 나타나는 위치(인덱스) 반환
- 찾는 문자가 없다면 **오류 발생**

``` python
word = "apple"

print(word.find("p"))
>> 1

print(word.find("K"))
>> ValueError
```
<br/>

## .count(개수를 셀 문자)
- 문자열에서 특정 문자가 몇 개인지 반환
- 문자열도 가능

``` python
word = "banana"

print(word.count("a"))
>> 3

print(word.count("na"))
>> 2
```


<br/>

## .replace(기존 문자, 새로운 문자)
- 문자열에서 특정한 값을 다른 값으로 치환하고 수정된 문자열 반환

``` python
word = "I wanna study"

replace_word = word.replace("study", "sleep")

print(replace_word)
>> I wanna sleep
```

- 특정 문자를 빈 문자열로 치환하여 해당 문자를 삭제한 효과도 가능

``` python
word = "abcdefg"

replace_word = word.replace("b", "")

print(replace_word)
>> acdefg
```

<br/>

## 삽입할 문자.join(iterable)
> iterable : string, list, tuple, range, set, dict
- iterable의 각각 문자 사이에 특정 문자를 삽입한 결과를 문자열로 반환

``` python
word = "abcdefg"

join_word = " ".join(word)

print(join_word)
>> a b c d e f g
```

- 삽입할 문자를 빈 문자열로 지정하여, 하나의 문자열로 합치는 효과

``` python
apple = ["a", "p", "p", "l", "e"]

join_word = "".join(apple)

print(join_word)
>> apple
```

❗ join의 인자인 iterable 자료형의 원소들은 문자열이어야 함 <br/>
원소들 중 문자열이 아닌 것이 있다면 오류 발생



<br/><br/>

--- 




<문제> 문자열 뒤집기

<br/>

<방법>

1. 반복문


``` python
# 1. 반복문을 이용한 문자열 뒤집기

string = 'Hello Algorithm'
reversed_string = ''

for i in range(len(string) - 1, -1, -1): # 맨 뒤에서부터 시작하여 처음까지
    reversed_string += string[i]

print(reversed_string)
```

2. reverse


``` python
# 2. list()와 .reverse()를 이용한 문자열 뒤집기

string = 'Hello Algorithm'

string_list = list(string)
string_list.reverse()
print(string_list)

reversed_string = ''.join(string_list) # 붙여준다

print(reversed_string)
```

3. 슬라이싱 -- 제일 빠름


``` python
# 3. 슬라이싱을 이용한 문자열 뒤집기

# 문자열[start, end, step]

string = 'Hello Algorithm'
reversed_string = string[::-1]

print(reversed_string)
```

---

int, str 쓰지 않고 문자열 <-> 정수 변환
- 노션 코드 참고

chr, ord 이용해서 아스키코드 상에서 숫자를 더하거나 빼면서 그 다음 문자로 이동 가능


---





