# Today I Learned
1. 할당
2. 얕은 복사
3. 깊은 복사

<br/>

> mutable vs. immutable  →  내용 수정 가능 여부
> 
> - mutable : 리스트, 셋, 딕셔너리
> 
> - immutable : 튜플, 레인지, bool, int, float, str

<br/>

``` python
a = [3, 1, 2]
a.sort()
print(a)  # [1, 2, 3]
# 리스트 - mutable

b = “hello”
b.replace(“h”, “j”)
print(b)  # hello
# str - immutable
``` 
<br/><br/>

--- 

## 📌 할당
- 두 변수가 같은 값을 공유

- 대입 연산자 (=)
  - 대입 연산자 (=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사

<img width="200" src= https://i.esdrop.com/d/f/GQtKpTuAPv/HW1TpgR2WN.png alt="할당">

``` python
a = [1, 2, 3]
b = a
print(a, b)  # [1, 2, 3] [1, 2, 3]

b[0] = 4
print(a, b)  # [4, 2, 3] [4, 2, 3]

# 두 리스트의 값이 함께 변경됨
```
<br/>

<img width="230" src= https://i.esdrop.com/d/f/GQtKpTuAPv/NA9yc6MAOY.png alt="할당">

``` python
a = "hello"
b = a
a += "python"
print(a, b)  # hellopython hello

# 문자열은 immutable --> 즉, a는 새로운 변수로 할당
```
### 💛mutable --> 같은 값에 포스트잇을 붙인 두 변수는 함께 바뀜
### 💚immutable --> 값이 바뀌지 않으므로 두 변수가 달라짐


<br/><br/>

---

## 📌 얕은 복사
- a와 b를 다르게 하고 싶을 때 => a와 똑같이 생긴 리스트 복사 후 b에 할당
- 즉, 다른 주소 / 내용물만 복사

<img width="230" src= https://i.esdrop.com/d/f/GQtKpTuAPv/hTUEmGwpta.png
alt="얕은복사">

``` python
a = [1, 2, 3]

# 방법1 
b = a[:]  # 슬라이싱 처음과 끝 생략 가능

# 방법2
b = list(a)

b[0] = 4
print(a, b)  # [1, 2, 3] [4, 2, 3]
```
<br/>

### But 

#### ❗ 얕은 복사 주의사항
- 복사하는 리스트의 원소가 주소를 참조하는 경우
- 2차원 리스트인 경우, 결과가 달라짐
<br/>

<img width="300" src= https://i.esdrop.com/d/f/GQtKpTuAPv/BrcVSW81Dx.png
alt="얕은복사_문제2">

<img width="270" src= https://i.esdrop.com/d/f/GQtKpTuAPv/4I3mZtrm7q.png
alt="얕은복사_문제">


``` python
a = [1, 2, [5, 6]]
b = a[:]
print(a, b)  # [1, 2, [5, 6]] [1, 2, [5, 6]]

a[2][0] = 7
print(a, b)  # [1, 2, [7, 6]] [1, 2, [7, 6]]

# 복사를 했는데 함께 바뀌어 있음
# 내부 리스트는 같은 곳을 보고 있음 (복사가 안됨)
```




<br/><br/>

---

## 📌 깊은 복사
- 통째로 복사
- copy.deepcopy()

``` python
a = [1, 2, [5, 6]]
b = copy.deepcopy(a)
print(a, b)  # [1, 2, [5, 6]] [1, 2, [5, 6]]

a[2][0] = 7
print(a, b)  # [1, 2, [7, 6]] [1, 2, [5, 6]]
```
<br/><br/>

---

### 이중 리스트와 (im)mutable
<br/>

``` python
a = [[0] * 3] * 3
a[0][0] = 1
print(a)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]


print(id(a[0]))  # 2090134809472
print(id(a[1]))  # 2090134809472
print(id(a[2]))  # 2090134809472


a = [[0] * 3 for i in range(3)]  # int는 immutable 이기 때문에 곱셈 사용 가능
print(a)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][0] = 1
print(a)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

