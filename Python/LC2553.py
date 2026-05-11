class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        separated_nums = []
        for n in nums:
            arr = []
            while n > 0:
               r = n % 10
               n //= 10
               arr.append(r)
            separated_nums += arr[::-1]
        return separated_nums 