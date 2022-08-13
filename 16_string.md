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





