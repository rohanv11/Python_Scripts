class Node:
    head = 0
    def __init__(self, value) -> None:
        self.value = value

from copy import deepcopy

n1 = Node(1)
n2 = Node(2)
print("NodeHead", Node.head)
Node.head = 5
print("NodeHead", Node.head)
print("newNodeHead", n1.head)
n1.head = 55
print("NodeHead", Node.head)
print("newNode1Head", n1.head)
print("newNode2Head", n2.head)
Node.head = 100
print("NodeHead", Node.head)
print("newNode1Head", n1.head)
print("newNode2Head", n2.head)

n5 = deepcopy(n1)
print(n5)