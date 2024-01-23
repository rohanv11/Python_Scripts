from copy import copy
class Node:
    def __init__(self, value):
        self.value = value
        self.nxt = None


def insert_node(head, idx, value):
    # @param idx, an integer
    # @param value, an integer
    print("idx", idx, "value", value)
    if head == None:
        print("FFFFFFFidx", idx, "value", value)
        if idx == 1:
            head = Node(value)
            return head
        else: # this else not needed
            return None
    else:
        print("LLLLLLLLLidx", idx, "value", value)
        temp = head
        if idx == 1:
            new_node = Node(value)
            new_node.nxt = temp
            return new_node
        else:
            prev = None
            count = 1
            for i in range(1, idx):
                print("insert count :", count)
                count += 1
                if not temp:
                    return head
                prev = temp
                temp = temp.nxt
                print(f"prev: {prev.value}")
                if temp:
                    print(f"temp: {temp.value}")
                
            # temp is your current node
            new_node = Node(value)
            prev.nxt = new_node
            new_node.nxt = temp
            return head

        


def delete_node(position):
    # @param position, integer
    # @return an integer
    pass


def print_ll(head):
    # Output each element followed by a space
    temp = head
    count = 1
    while temp:
        print(f"{temp.value}//{count}-", end = "")
        count += 1
        temp = temp.nxt
    print()

_input = ["i 1 2", "i 2 4", "i 3 6"]
n = int(len(_input))
head = None
for i in range(n):
    row = _input[i].split(" ")
    op = row[0]
    if op == "i":
        idx = int(row[1])
        value = int(row[2])
        head = insert_node(head, idx, value)
    
    print_ll(head)
    # elif op == "p":
    #     print_ll(head)
    

