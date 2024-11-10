class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bits = [0] * 32
        cur = left = 0
        res = len(nums) + 1

        for right in range(n):
            cur |= nums[right]

            for bit in range(32):
                if nums[right] & (1 << bit):
                    bits[bit] += 1
            
            while left <= right and cur >= k:
                res = min(res, right - left + 1)
                next = 0
                for bit in range(32):
                    if nums[left] & (1 << bit):
                        bits[bit] -= 1
                    if bits[bit] > 0:
                        next |= (1 << bit)
                cur = next
                left += 1
        return res if res <= len(nums) else -1