def pre(n):
    if n <= size:
        print(tree[n])
        pre(2 * n)
        pre(2 * n + 1)


tree = [0, 'A', 'B', 'C', 'D', 'E', 'F']  # 완전이진트리
size = len(tree) - 1  # 마지막 정점 번호

pre(1)

'''
A
B
D
E
C
F
'''
