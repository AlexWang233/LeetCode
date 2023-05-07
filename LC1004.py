class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = end = 0
        count = 0
        ans = 0
        for i in nums:
            if i == 0:
                count += 1
            if count > k:
                print(end)
                while start <= end:
                    start += 1
                    if nums[start - 1] == 0:
                        break
                count -= 1
            ans = max(ans, end - start + 1)
            end += 1
        return ans