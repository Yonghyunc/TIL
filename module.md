# 지나가다 마주친 다양한 모듈 사용법

## random 모듈

- **random.choice**(리스트, k=취득 개수)
  - 중복 있이 랜덤 추출
  - k가 리스트의 요소 수보다 커도 O


- **random.sample**(리스트, 취득 개수)
  - 중복 없이 랜덤 추출
  - 결과값은 리스트 형태로 반환


- **random.randint**(start, end)
  - 두 개의 수 사이 정수 난수 반환


- **random.uniform**(start, end)
  - 두 개의 수 사이 실수 난수 반환


- **random.randrange**(start, end, step)
  - 두 개의 수 사이 step 간격으로 된 수들 중 정수 난수 반환
  - 난수 범위에 end 포함 X


- **random.shuffle**(iterable)
  - iterable 객체 원본의 순서를 바꿔서 반환


