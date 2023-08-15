class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        def pow(x, n):
            ans = 1
            while n > 0:
                if n % 2 == 1:
                    ans *= x
                    ans %= mod
                x = (x * x) % mod
                n //= 2
            return ans
        l = len(nums)
        upper = max(nums) + 1
        prime = [True] * upper
        prime[0] = prime[1] = False
        primeCount = [0]*upper
        for i in range(2, upper):
            if prime[i]:
                for j in range(i, upper, i):
                    primeCount[j] += 1
                    prime[j] = False

        prevArr = [l] * l
        temp = []
        for i in range(l):
            while temp and primeCount[nums[i]] > primeCount[nums[temp[-1]]]:
                temp.pop()
            prevArr[i] = temp[-1] if temp else -1
            temp.append(i)

        nextArr = [l] * l
        temp = []
        for i in range(l-1, -1, -1):
            while temp and primeCount[nums[i]] >= primeCount[nums[temp[-1]]]:
                temp.pop()
            nextArr[i] = temp[-1] if temp else l
            temp.append(i)

        res = 1
        tuples = [(nums[i], i) for i in range(l)]
        tuples.sort(reverse=True)
        for n, i in tuples:
            ops = min((i - prevArr[i]) * (nextArr[i] - i), k)
            res = (res * pow(n, ops)) % mod
            k -= ops
            if k == 0:
                break

        return res
