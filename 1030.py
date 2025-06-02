class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res=[]
        for r in range(rows):
            for c in range(cols):
                dis=abs(r-rCenter)+abs(c-cCenter)
                res.append([r,c,dis])
        res.sort(key=lambda x:x[2])
        return [[r,c] for r , c,_ in res]