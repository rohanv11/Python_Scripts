class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2

temp = n1
while temp:
	print(temp.val)
	temp.val = -99
	temp = temp.next

print(n1.next, n1.val)

l1 = [1, 2, 3, 4, 5]
l5 = [5,6]

l2 = l1

l2.pop()

l2 = l5

print(l1)
print(l2)