for t in range(1, int(input()) + 1):
    brackets = input()
    stack = []
    result = -1  # 일단 불가능 상태로 초기화

    for bracket in brackets:
        # 1. 여는 괄호인 경우
        if bracket == '(':
            stack.append(bracket)  # 스택에 넣음
        # 2. 닫는 괄호인 경우
        else:
            if not stack:
                break  # 닫는 괄호인데 스택이 비었다는 건 짝이 맞지 않는다는 것이므로 그대로 종료
            stack.pop()  # 닫는 괄호가 나왔으므로 스택에 들어있는 여는 괄호를 제거
    else:
        if not stack:
            result = 1  # 반복문이 정상 종료 되었을 때, 스택이 비어있다는 건 괄호의 짝이 맞는다는 것임

    print(f'#{t} {result}')
