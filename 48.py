class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        print(m)
        res=[]
        l=[]
        for i in range(m):
            for j in range(m-1,-1,-1):
                l.append(matrix[j][i])
            res.append(l)
            l=[]
        return res

m=[[1,2,3],[4,5,6],[7,8,9]]
s=Solution()
print(s.rotate(m))