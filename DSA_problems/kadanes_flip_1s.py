"""
You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
"""

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        zeros = 0
        for ch in A:
            if ch == "0":
                zeros += 1
        
        if zeros == 0:
            return []
        n = len(A)
        l = 0
        r = 0
        csum = 0
        max_sum = 0
        ans = [0, 0]

        # common code for kadane inside the loop
        for i in range(n):
            if A[i] == "1":
                csum -= 1
            else:
                csum += 1

            if csum > max_sum:
                max_sum = csum
                ans[0] = l + 1
                ans[1] = r + 1

            if csum < 0:
                csum = 0
                l = i + 1
                r = i + 1
            else:
                r += 1
        
        if max_sum == 0:
            return []
        return ans



        