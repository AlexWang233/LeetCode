class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [1, 1]
        if rowIndex == 1:
            return row
        
        while rowIndex > 1:
            rowIndex -= 1
            prevRow = row.copy()
            for i in range(len(row)-1):
                row[i+1] = prevRow[i+1] + prevRow[i]
            row.append(1)
            
        return row
            
        