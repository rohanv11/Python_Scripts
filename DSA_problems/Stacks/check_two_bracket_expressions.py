class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        map_1 = get_sign_map(A)
        map_2 = get_sign_map(B)
        
        return 1 if map_1 == map_2 else 0




def get_sign_map(A):
    from collections import deque
    stack = deque()
    # if A[0] == "+" or A[0] == "-":
    #     stack.append(A[0])
    # else:
    stack.append("+")
    _map = {}
    OPEN = "("
    CLOSE = ")"

    for idx, ch in enumerate(A):
        # print("stack", stack)
        # print("idx ch", idx, ch)
        if ch == OPEN:
            update_stack(stack, A, idx)
            continue
        
        if ch == CLOSE:
            stack.pop()
            continue

        if ch == "+":
            continue
        
        if ch == "-":
            continue

        # at this stage the ch value will be a to z
        sign = evaluate_sign(stack, A, idx)
        _map[ch] = sign
        # print("_map", _map)
        # print("stack", stack, "\n")

    return _map


def update_stack(stack, A, idx):
    top = stack[-1]
    if idx == 0:
        stack.append(top)
        return
    
    sign = evaluate_sign(stack, A, idx)

    stack.append(sign)
    return

def evaluate_sign(stack, A, idx):
    top = stack[-1]
    
    if idx == 0:
        return top
    
    adj = A[idx - 1]
    if adj == "(" or adj == "+":
        return top
    
    if adj == "-":
        if top == "-":
            return "+"

        
        if top == "+":
            return "-"
    
