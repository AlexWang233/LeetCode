class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i]:
                    baskets[j] = 0
                    fruits[i] = 0
                    break
            if fruits[i] > 0:
                ans += 1
        return ans
