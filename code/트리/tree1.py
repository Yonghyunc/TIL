'''
정점 번호 V : 1 ~ (E+1)
간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''

# 전위순회
def preorder(n):
    if n:
        print(n)  # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])


# 중위순회
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])


# 후위순회
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)


E = int(input())
arr = list(map(int, input().split()))
V = E + 1
root = 1
# 부모를 인덱스로 자식 번호 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:  # 아직 자식이 없으면
        ch1[p] = c
    else:
        ch2[p] = c
print(ch1)  # [0, 2, 0, 4, 0, 0]
print(ch2)  # [0, 3, 0, 5, 0, 0]

preorder(root)  # 1 2 3 4 5
inorder(root)  # 2 1 4 3 5
postorder(root)  # 2 4 5 3 1

'''
for j in range(0, E*2, 2):
    p, c = arr[j], arr[j + 1]
도 사용 가능
'''
