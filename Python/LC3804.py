class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = defaultdict(lambda: 0)

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.sheet:
            del self.sheet[cell]

    def getValue(self, formula: str) -> int:
        arr = formula[1:].split('+')
        ans = 0
        for n in arr:
            if n.isdigit():
                ans += int(n)
            else:
                ans += self.sheet[n]
        return ans


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)