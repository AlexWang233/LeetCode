class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.arr = []

        def bt(k, cur):
            s = sum(self.arr)
            if k == 0 and s == n:
                self.ans.append(self.arr.copy())
            for i in range(cur + 1, min(10, n - s + 1)):
                self.arr.append(i)
                bt(k - 1, i)
                self.arr.pop()

        bt(k, 0)
        return self.ans
