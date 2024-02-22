class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = [-1 for _ in range(A - 1)]
        heap = build_heap(B, A)
        ans.append(heap[0])
        print(heap)
        print(ans)

        for i in range(A, len(B)):
            conditional_update_heap(heap, B, i)
            ans.append(heap[0])
            print(heap)
            print("ans", ans)
        
        return ans
    
def conditional_update_heap(heap, arr, idx):
    if heap[0] < arr[idx]:
        remove_from_heap(heap)
        insert_onto_heap(heap, arr[idx])

    return


def remove_from_heap(heap):
    swap(heap, 0, len(heap) - 1)
    heap.pop()

    i = 0
    down_heapify(heap, i)




def insert_onto_heap(heap, value):
    if not len(heap):
        heap.append(value)
        return
    
    up_heapify(heap, value)

def up_heapify(heap, value):
    heap.append(value)
    i = len(heap) - 1

    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] > heap[i]:
            swap(heap, parent, i)
            i = parent
        else:
            break
    
    return






def build_heap(arr, elems):
    n = elems - 1
    parent = (n - 1) // 2
    heap = arr[:elems]
    for i in range(parent, -1, -1):
        down_heapify(heap, i)
    
    return heap



def down_heapify(heap, i):
    lc = (2 * i) + 1
    rc = (2 * i) + 2

    if lc >= len(heap):
        return
    
    if rc >= len(heap):
        if heap[i] > heap[lc]:
            swap(heap, i, lc)
        return 

    if heap[lc] < heap[rc]:
        smaller = lc
    else:
        smaller = rc
    
    if heap[i] > heap[smaller]:
        swap(heap, i, smaller)
        down_heapify(heap, smaller)
    
    return

def swap(A, idx1, idx2):
    temp = A[idx1]
    A[idx1] = A[idx2]
    A[idx2] = temp 