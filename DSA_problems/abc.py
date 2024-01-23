class Solution:
	# @param A : integer
	# @return a strings
	def convertToTitle(self, A):
        ans = []
        A_ord = ord("A")
        while A > 0:
            rem = A % 26
            if rem == 0:
                c = "Z"
            else:
                c = chr(A_ord + rem - 1)
            print(c)
            ans.append(c)
            A = A // 26

        ans = "".join(ans[::-1])
        return ans
      

s = Solution()
print(s.convertToTitle(943566))
