class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            elif len(d) < 3:
                d[n] = 1
            else:
                temp = {}
                for c in d:
                    d[c] -= 1
                    if d[c] >= 1:
                        temp[c] = d[c]
                d = temp

        res = []
        for n in d:
            if nums.count(n) > len(nums) // 3:
                res.append(n)

        return res