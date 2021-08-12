#출처[https://jm-codingmemo.tistory.com/22]
import sys
 
N = int(sys.stdin.readline().strip())
tree = {}
 
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]
 
 
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
 
 
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()

# n = int(input())
# a = {}
# for _ in range(n):
#     nodes = list(map(str, input().split()))
#     if nodes[0] not in a.keys():
#         a[nodes[0]] = nodes[1:]

# answer = 'A'
# def preorder(node):
#     global answer
#     if a[node][0] != '.':
#         new_node = a[node][0]
#         answer += new_node
#         a[node][0] = '.'
#         preorder(new_node)

#     elif a[node][1] != '.':
#         new_node = a[node][1]
#         answer += new_node
#         a[node][1] = '.'
#         preorder(new_node)


# for node in a.keys():
#     preorder(node)

# print(a)
# print(answer)