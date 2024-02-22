# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# also solve this using deque
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        heap = []
        for head in A:
            insert_into_heap(heap, head)
        # print_heap(heap)
        # print(len(A))
        val = remove_and_insert(heap)
        ans = []
        ans.append(val)
        ans_head = ListNode(val)
        current = ans_head
        while not check_if_heap_empty(heap):
            # print("ans", ans)
            val = remove_and_insert(heap)
            ans.append(val)
            current.next = ListNode(val)
            current = current.next
        

        while len(heap):
            # print(heap)
            head_to_pop = remove_from_heap(heap)
            val = head_to_pop.val
            ans.append(val)
            current.next = ListNode(val)
            current = current.next


        # print(ans)
        return ans_head

def check_if_heap_empty(heap):
    for item in heap:
        if item.next:
            return False
        
    return True


def remove_and_insert(heap):
    head_to_pop = remove_from_heap(heap)
    # print("head_to_pop", head_to_pop.val, head_to_pop.next)
    # print_heap(heap)
    if not head_to_pop:
        return
    ans = head_to_pop.val
    
    if head_to_pop.next:
        insert_into_heap(heap, head_to_pop.next)
    return ans


def remove_from_heap(heap):
    if not len(heap):
        return
    
    if len(heap) == 1:
        return heap.pop()
    
    ans = heap[0]
    swap(heap, 0, len(heap) - 1)
    heap.pop()

    i = 0
    while i < len(heap) - 1:
        lc = (2 * i) + 1
        rc = (2 * i) + 2

        if lc >= len(heap):
            break
        
        if rc >= len(heap):
            if heap[i].val > heap[lc].val:
                swap(heap, i, lc)
            break


        if heap[lc].val < heap[rc].val:
            to_swap_idx = lc
        else:
            to_swap_idx = rc

        
        if heap[i].val > heap[to_swap_idx].val:
            swap(heap, i, to_swap_idx)
            i = to_swap_idx
        else:
            break
        
    return ans



def insert_into_heap(heap, head):
    if not len(heap):
        heap.append(head)
        return
    
    heap.append(head)
    i = len(heap) - 1

    while i > 0:
        parent_idx = (i - 1) // 2

        if heap[parent_idx].val > heap[i].val:
            swap(heap, parent_idx, i)
            i = parent_idx
        else:
            break

def swap(heap, idx1, idx2):
    temp = heap[idx1]
    heap[idx1] = heap[idx2]
    heap[idx2] = temp


def print_heap(heap):
    for item in heap:
        print(item.val, end = " ")
    print("\n")