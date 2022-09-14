# 연습문제
'''
정점의 개수 : 13
1 2 1 3 2 4 3 4 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i


# 전위순회
def preorder(n):
    if n:
        print(n, end=' ')  # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])


# 중위순회
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n, end=' ')
        inorder(ch2[n])


# 후위순회
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')


# global cnt 없이 순회한 정점 수를 리턴하는 함수
def f(n):
    if n == 0:  # 서브트리가 비어있으면
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1


V = int(input())  # 정점 개수, 마지막 정점 번호
arr = list(map(int, input().split()))
E = V - 1

# 부모를 인덱스로 자식 번호 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
# 자식을 인덱스로 부모 번호 저장
par = [0] * (V + 1)
for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p

root = find_root(V)
# print(root)   # 1
preorder(root)  # 1 2 4 7 12 3 4 7 12 6 10 11 13
print()
inorder(root)  # 12 7 4 2 1 12 7 4 3 10 6 13 11
print()
postorder(root)  # 12 7 4 2 12 7 4 10 13 11 6 3 1

print()
print(f(root))

# 주어진 트리를 root부터 전위 / 중위 / 후휘 순회하는 경우, 각각 마지막 정점은?
'''
def preorder(n):
    global cnt
    if n:
        cnt = n
        preorder(ch1[n])
        preorder(ch2[n])
'''
