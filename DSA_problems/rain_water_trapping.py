class Solution:
	# @param A : tuple of integers
	# @return an integer
    def trap(self, A):
        left_max_idx = 0
        right_max_idx = 2
        n = len(A)
        ans = 0
        count = 0

        for i in range(1, len(A)-1):
            if A[i] > A[left_max_idx]:
                left_max_idx = i
            
            if i == right_max_idx:
                right_max_idx = i + 1
            
            if A[right_max_idx] < A[left_max_idx]:
                right_max_idx = get_max(left_max_idx, right_max_idx, A, n)
            
            count+=1
            # print("No.", count)
            # print("left_max_idx", left_max_idx, "right_max_idx", right_max_idx)
            # print("left_max", A[left_max_idx], "right_max", A[right_max_idx])
            
            left_max = A[left_max_idx]
            right_max = A[right_max_idx]

            fill_capacity = min(left_max, right_max)
            water = fill_capacity - A[i]
            if water < 0:
                water = 0
            ans += water
            # print("A[i]",A[i], "water", water, "ans",ans)
            # print("\n\n")

        return ans
       

def get_max(left_max_idx, right_max_idx, A, n):
    idx = right_max_idx
    is_updated = False
    for i in range(right_max_idx+1, n):
        if A[i] > A[left_max_idx]:
            return i
        elif A[i] >= A[idx]:
            idx = i
            is_updated = True
        elif i == n-1:
            if not is_updated:
                return i

    return idx




# def get_max_prefix(A):
#     pref = []
#     pref.append(A[0])
#     for i in range(1, len(A)):
#         pref.append( pref[i-1] if pref[i-1] > A[i] else A[i])
#     return pref

# def get_max_suffix(A):
#     suff = [item for item in A]
#     for i in range(len(suff)-2, -1, -1):
#         suff[i] = suff[i+1] if suff[i+1] > suff[i] else suff[i]
#     return suff

# _input = [0,1,0,2,1,0,1,3,2,1,2,1]
_input = [8,71,58,31,89,18,67,35,53,100,42,11,64,98,55,4,8,62,75,15,65,90,0,94,53,46,38,47,41,54,36,93,60,77,72,35,96,100,94,53,12,57,41,83,12,9,72,66,90,19,12,8,14,41,89,84,31,28,95,11,99,44,89,68,60,73,55,87,25,61,30,65,71,5,9,14,74,23,58,69,36,14,84,82,36,11,83,50,61,45,84,30,40,0,99,42,85,7,63,96,62,44,92,73,0,40,96,24,82,95,83,72,51,13,53,25,90,33,51,22,38,43,25,10,36,87,74,84,79,11,47,75,11,47,34,30,89,55,42,82,71,50,89,27,64,52,59,5,35,88,0,62,15,39,34,17,87,55,44,82,85,100,19,85,61,10,75,38,6,26,66,29,26,63,58,84,91,45,86,28,85,63,10,56,70,97,57,64,3,2,41,98,5,6,3,93,3,21,64,49,93,18,68,63,63,81,58,20,26,32,12,31,14,100,7,80,15,47,95,53,86,57,74,11,30,86,87,76,15,9,94,20,31,56,79,82,55,99,22,64,56,85,32,38,97,23,80,94,45,90,62,92,37,29,6,65,45,21,26,45,37,0,95,76,81,13,63,42,36,77,78,68,64,14,10,43,21,69,23,22,55,88,16,4,55,2,36,31,32,6,15,21,53,70,44,42,56,92,37,94,89,40,57,27,63,47,74,4,13,53,97,50,49,12,56,83,29,91,48,89,20,39,85,59,58,35,51,9,62,41,5,3,47,7,78,34,5,69,66,17,27,5,59,10,39,21,7,97,50,71,73,90,59,43,71,71,19,11,79,20,96,25,15,24,94,81,20,52,72,96,57,55,11,73,39,55,18,6,86,40,89,80,85,99,66,64,73,0,79,57,16,32,10,32,12,7,90,70,92,95,6,39,46,52,11,94,3,37,47,33,81,78,40,83,84,26,5,16,0,39,95,61,4,61,63,49,71,47,30,21,53,13,63,55,24,0,45,90,6,37,34,62,6,53,79,51,30,98,0,30,74,26,16,65,79,80,4,78,32,43,80,39,28,95,84,55,73,55,84,96,34,100,14,48,61,59,32,31,27,31,57,82,3,1,72,19,64,30,89,31,88,32,44,5,20,38,29,81,60,53,14,22,14,14,94,16,76,57,31,59,85,71,90,36,88,75,37,46,66,2,12,70,88,93,96,99,37,61,53,93,50,89,11]
correct = 26197

if __name__ == "__main__":
    ans = Solution().trap(_input)
    print("Ans", ans)