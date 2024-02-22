class Solution:
    # @param A: list of integers
    # @return: a list representing the binary min heap
    def build_heap(self, A):
        # code here
        n = len(A) - 1
        last_parent = (n - 1) // 2
        for i in range(last_parent, -1, -1):
            down_heapify(A, i)

        return A
    

def down_heapify(A, i):
    lc = (2 * i) + 1
    rc = (2 * i) + 2
    if lc >= len(A) and rc >= len(A):
        return
    
    if lc >= len(A):
        if A[rc] < A[i]:
            swap(A, rc, i)
        return
    
    if rc >= len(A):
        if A[lc] < A[i]:
            swap(A, lc, i)
        return
    
    if A[lc] < A[rc]:
        smaller = lc
    else:
        smaller = rc

    
    if A[smaller] < A[i]:
        swap(A, smaller, i)
        down_heapify(A, smaller)

    return

def swap(A, idx1, idx2):
    temp = A[idx1]
    A[idx1] = A[idx2]
    A[idx2] = temp 