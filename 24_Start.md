# Today I Learned
- SW 문제 해결 과정
- 복잡도 분석
- 비트 연산
- 진수

<br><br>

---

# SW 문제 해결 과정
1. 문제를 읽고 이해한다
2. 문제를 익숙한 용어로 재정의한다
3. 어떻게 해결할지 계획을 세운다
4. 계획을 검증한다
5. 프로그램으로 구현한다
6. 어떻게 풀었는지 돌아보고, 개선할 방법이 있는지 찾아본다


<br><br>

---

# 복잡도 분석  

🔹 알고리즘 : 문제를 해결하기 위한 절차나 방법  
🔹 알고리즘의 효율
- 공간적 효율성 : 연산량 대비 얼마나 적은 메모리 공간을 요하는가
- 시간적 효율성 : 연산량 대비 얼마나 적은 시간을 요하는가

**복잡도(complexiy) <-> 효율성**

<br>

🔹 시간적 복잡도 분석  
복잡도의 점근적 표기  
➡ 입력 크기 n이 무한대로 커질 때의 복잡도를 간단히 표현하기 위해 사용  
- Big-O   
  - 복잡도의 점근적 상한 
- Big-Omaga  
  - 복잡도의 점근적 하한 (최소한 이만한 시간은 걸린다)
- Big-Theta

> 표기방법은 같은데, 해석이 다름  
> O : 최악의 경우에는 그걸 넘어가지는 않아  
> Omega : 그건 넘을거야

<br>

🔹 자주 사용하는 O-표기

|            |                |
| :--------: | :------------: |
|    O(1)    |   상수 시간    |
|  O(log n)  |   로그 시간    |
|    O(n)    |   선형 시간    |
| O(n log n) | 로그 선형 시간 |
|   O(n^2)   |   제곱 시간    |
|   O(n^3)   |  세제곱 시간   |
|   O(2^n)   |   지수 시간    |


<br>

🔹 왜 효율적인 알고리즘이 필요 ?  
➡ 효율적인 알고리즘은 슈퍼컴퓨터보다 더 큰 가치가 있다 (훨씬 경제적)


<br><br>

---

# 표준 입출력 방법
### Python3 표준입출력  
<br>

🔹 입력
- raw 값 입력 : input()
  - 받은 입력값을 문자열로 취급
- evaluated된 값 입력 : eval(input())
  - 받은 입력값을 평가된 데이터 형으로 취급  

<br>

🔹 출력
- print() : 표준 출력 함수, 출력값의 마지막에 개행 문자 포함
- print('text', end='') : 마지막의 개행문자 제거
- print('%d' % number) : Formatting 된 출력

<br>

🔹 파일의 내용을 표준 입력으로 불러오는 방법  
  ``` python
  import sys  
  sys.stdin = open("a.txt", "r") 
  ``` 

> ❕ 반드시 써야하는 경우  
> pycharm의 console에 복사-붙여넣기 크기 1MB로 제한
> ➡ 1MB가 넘어가는 대용량의 파일은 console 창에 붙여넣기 불가


<br><br>

---

# 비트 연산

1 byte = 8 bit  
메모리에 주소가 부여되는 단위 : 8 bit  
비트 연산은 같은 비트 번호끼리 연산하고 끝남  

<br>

🔹 비트 연산자  
<img width="500" src=https://user-images.githubusercontent.com/93974908/190975878-23891c84-ee2d-474d-998a-f8b03e815393.png alt="비트연산자">

<br>

✅ & 연산자 (AND)  
- bit & 0 = 0   
- bit & 1 = 원래의 bit  

    |       |       |
    | :---: | :---: |
    | 0 & 0 |   0   |
    | 0 & 1 |   0   |
    | 1 & 0 |   0   |
    | 1 & 1 |   1   |

  > 특정 비트를 0으로 만들 때  
  > 비트 검사  
 
<br>

✅ | 연산자 (OR)  
- bit | 0 = 원래의 bit  
- bit | 1 = 1 

    |            |       |
    | :--------: | :---: |
    | 0 &#124; 0 |   0   |
    | 0 &#124; 1 |   1   |
    | 1 &#124; 0 |   1   |
    | 1 &#124; 1 |   1   |

    > 특정 bit를 1로 만들 때

<br>

✅ ^ 연산자 (OR)  
- 같으면 0, 다르면 1


    |       |       |
    | :---: | :---: |
    | 0 ^ 0 |   0   |
    | 0 ^ 1 |   1   |
    | 1 ^ 0 |   1   |
    | 1 ^ 1 |   0   |


  > 특정 bit를 반전시킬 때  


  > bit = 0 if bit else 1  
  > bit = bit ^ 1  
  > bit ^= 1  

<br>

✅ 시프트 연산자  
- 왼쪽 시프트 : 옮겨가는 만큼 2의 제곱수를 곱해주는 것과 동일  
- 오른쪽 시프트 : 나눠주는 것과 동일  


    1 : 0 0 0 1  << 1  
    2 : 0 0 1 0  
    1 : 0 0 0 1  << 1  
    4 : 0 1 0 0 

    2 : 0 0 0 1 0 << 2  
    8 : 0 1 0 0 0  


<br><br>


🔹 1 << n  
2^n의 값을 가짐  
원소가 n개일 경우의 모든 부분집합의 수  
Power set (모든 부분 집합)  
- 각 원소가 포함되거나 포함되지 않는 2가지 경우의 수를 계산하면 모든 부분집합의 수 계산 O  

<br>

🔹 i & (1 << j)  
i의 j번 비트 검사  
(i의 j번째 비트가 1인지 아닌지)  

<br>

🔹 비트 연산 예제 0  
10진수를 4비트 2진수로 바꾸는 함수  
주로 16진수를 10진수로 바꾼 뒤 2진수로 바꿀 때 사용
``` python
def Bbit(i):
    output = ""
    for j in range(3, -1, -1):
        output += '1' if i & (1 << j) else '0'
    return output
```

<br>

🔹 비트 연산 예제 1
``` python
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)

for i in range(-5, 6):
    print("%3d = " % i, end='')
    Bbit_print(i)


# result
'''
 -5 = 11111011
 -4 = 11111100
 -3 = 11111101
 -2 = 11111110
 -1 = 11111111
  0 = 00000000
  1 = 00000001
  2 = 00000010
  3 = 00000011
  4 = 00000100
  5 = 00000101
'''
```

<br>

🔹 비트 연산 예제 2
``` python
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output, end=' ')

a = 0x10        # 1 byte
x = 0x01020304  # 4 byte
print("%d = " % a, end='')
Bbit_print(a)
print()
print("0%X = " % x, end='')
for i in range(0, 4):
    Bbit_print((x >> i*8) & 0xff)


# result 
'''
16 = 00010000 
01020304 = 00000100 00000011 00000010 00000001 
'''
```

<br><br>

🔹 엔디안 (Endianness)  
컴퓨터의 메모리와 같은 1차원의 공간에 여러 개의 연속된 대상을 배열하는 방법  
빅 엔디안 : 보통 큰 단위가 앞에 나옴 (네트워크)  
리틀 엔디안 : 작은 단위가 앞에 나옴 (대다수 데스크탑 컴퓨터)  

|    종류     | 0x1234 | 0x12345678  |
| :---------: | :----: | :---------: |
|  빅 엔디안  | 12 34  | 12 34 56 78 |
| 리틀 엔디안 | 34 12  | 78 56 34 12 |

<br>

엔디안 확인 코드
``` python 
import sys

print(sys.byteorder)
```

<br><br>

🔹 비트 연산 예제 3
``` python
# change endian

def ce(n):    
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i*8)) & 0xff)
    return p

x = 0x01020304
p = []
for i in range(0, 4):
    p.append((x >> (i*8)) & 0xff)

print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))
p = ce(x)
print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))


# result
'''
x = 4321
x = 1234
'''
```

<br>


🔹 비트 연산 예제 4
``` python
def ce1(n):
    return (n << 24 & 0xff000000) | (n << 8 & 0xff0000) | (n >> 8 & 0xff00) | (n >> 24 & 0xff)

x = 0x01020304
ce1(x)


# result
'''
x = 4321
x = 1234
'''
```
> (n << 24 & 0xff000000) : 04 자리에 마킹 (01에 넣어서 옮김)  
>> 04 00 00 00   

> (n << 8 & 0xff0000) : 03 자리에 마킹   
>> 00 03 00 00   

> (n >> 8 & 0xff00) : 02 자리에 마킹    
>> 00 00 02 00   

> (n >> 24 & 0xff) : 01 자리에 마킹  
>> 00 00 00 01  

<br>

🔹 비트 연산 예제 5
``` python
# 비트 연산자 ^를 두 번 연산하면 처음 값 반환

def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)
a = 0x86
key = 0xAA

print("a      ==> ", end='')
Bbit_print(a)

print("a^key  ==> ", end='')
a ^= key;
Bbit_print(a)

print("a^key  ==> ", end='')
a ^= key;
Bbit_print(a)


# result
'''
a      ==> 10000110
a^key  ==> 00101100
a^key  ==> 10000110
'''
```

<br><br>

---

# 진수
2진수, 8진수, 10진수, 16진수  

<br>

### ◾ 10진수 ➡ 타 진수로 변환  
원하는 타진법의 수로 나눈 뒤 나머지를 거꾸로 읽음

<br>

### ◾ 2진수, 8진수, 16진수 간 변환
2진법 ➡ 8진법 : 3자리씩 묶음  
8진법 ➡ 2진법 : 3자리씩 나열  

2진법 ➡ 16진법 : 4자리씩 묶음  
16진법 ➡ 2진법 : 4자리씩 나열  

<br>

### ◾ 컴퓨터에서의 음의 정수 표현 방법
1의 보수 : 부호와 절대값으로 표현된 값을 부호 비트를 제외한 나머지 비트들을 0은 1로, 1은 0으로 변환  
- -6 : 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 : 부호와 절대값 표현  
- -6 : 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 : 1의 보수 표현  
> 원래값 + 1의 보수 = 1

2의 보수 : 1의 보수방법으로 표현된 값의 최하위 비트에 1을 더함
- -6 : 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 : 2의 보수 표현
> 반전시켜 + 1