T = int(input()) # 첫번째 입력

for test_case in range(1, T + 1): #테스트 케이스 반복 횟수
    print(f'#{test_case}') 
    # 마지막 해결 구간: # 뒤에 띄어쓰기가 없어야 함
    # print("#", test_case)를 할 시 띄어쓰기가 자동 생성됨
    t = int(input()) # 두번째 입력
    a = '' # 빈 변수 생성

    for x in range(1, t + 1):
        lst = list(map(str, input().split())) 
        # 세번째 입력 (리스트 필수 아님!!)
        # eng, num = input.split()으로 간단히 받을 수 있음
        eng = str(lst[0])
        num = int(lst[1])
        res = eng * num
        a += res # 변수가 일렬로 나오도록 더해줌
    for y in range(0, len(a)+1,10): 
        # 문제가 되었던 구간: range(0, len(a)+1)만 하면 y가 계속 출력되어 케이스 사이 공백이 많이 생김
        print(a[0:10])
        a = a[10:]