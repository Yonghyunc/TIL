# Today I Learned



<br/>

---

# CSS Layout
- Display
- Position
- Float
- Flexbox
- Grid
- 기타
> 뭐가 더 좋다 라고 말하기는 어려움
<br/>

**어떤 요소를 감싸는 형태로 배치는?** <br/>
**혹은 좌/우측 배치는?** <br/>

## Float
- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 감싸도록 함
- 요소가 Normal flow를 벗어나도록 함
<img width="300" src=https://i.esdrop.com/d/f/GQtKpTuAPv/I3MjkozhT7.png alt="float">

  - none (기본값)
  - left
  - right

 #### 🔗 [float.html]()

<br/>
 
 ## Flex box (Flexible Box Layout)
- 1차원 레이아웃 모델

 #### 🔗 [flexbox.html]()

<br/>

- 축
  - main axis
  - cross axis

  <img width="300" src=https://i.esdrop.com/d/f/GQtKpTuAPv/ivWoz39UrX.png alt="flex-axis">

<br/>

- 구성 요소
  - flex container (부모 요소)
  - flex item (자식 요소)

<br/>

이전까지 normal flow를 벗어나는 수단은 Float 혹은 Position  ➡️ 불편함 <br/>

(수동 값 부여 없이) <br/>
1 ) 수직 정렬 <br/>
2 ) 아이템의 너비와 높이 혹은 간격을 동일하게 배치 <br/>

가 어려웠음 <br/>

   ⬇️ <br/>
부모 요소에 display: flex / inline-flex 적용하여 원하는 레이아웃 만들 수 있음

<br/><br/>

### Flex 속성
1. 배치 설정
- **flex-direction**
  - main axis 기준 방향 설정
  - 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의
  1. row
  2. row-reverse
  3. column
  4. column-reverse 

    <img width="500" src=https://i.esdrop.com/d/f/GQtKpTuAPv/sRPyKHl7f5.png alt="flex-direction">
<br/>

- **flex-wrap**
  - 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
  1. wrap : 넘치면 줄 바꿈
  2. nowrap: 한 줄에 끼워넣기
  3. wrap-reverse

    <img width="280" src=https://i.esdrop.com/d/f/GQtKpTuAPv/UsmTcNINnp.png alt="flex-wrap">
<br/>


2. 공간 나누기
- **justify-content** (Main axis 기준)
  1. flex-start
  2. flex-end
  3. center
  4. sapce-between : 사이의 간격이 같게
  5. sapce-around : 아이템을 둘러싼 각 여백이 전부 같게
  6. space-evenly : 전체 영역에서 아이템 간 간격을 전부 같게

    <img width="500" src=https://i.esdrop.com/d/f/GQtKpTuAPv/FGtqlugiTQ.png alt="justify-content">
<br/>


- **align-content**(cross axis 기준)
  - 아이템이 한 줄로 배치되는 경우 확인할 수 없음

  <img width="500" src=https://i.esdrop.com/d/f/GQtKpTuAPv/LpCEZXVxLg.png alt="align-content">
<br/>



3. 정렬
- **align-items** (모든 아이템을 cross axis 기준으로)
  1. stretch : 위아래로 늘리기
  2. flex-start : 위로
  3. flex-end : 아래로
  4. center : 가운데
  5. baseline : 글자 선으로 맞춤

    <img width="500" src=https://i.esdrop.com/d/f/GQtKpTuAPv/eOfmRbQD3I.png alt="align-items">
<br/>



- **align-self** (개별 아이템)

    <img width="500" src=https://i.esdrop.com/d/f/GQtKpTuAPv/fn0V10LVqd.png alt="align-self">
<br/>



1. 기타 속성

- flex-grow : 남은 영역(여백)을 아이템에 분배
- order : 배치 순서


