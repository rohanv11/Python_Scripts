class Node:
    head = 0
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

from copy import deepcopy

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3

print(n1.value)

n5 = deepcopy(n1)
print(n5)
