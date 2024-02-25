class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def dfs(i):
            nonlocal visitedIndex, visitedPrime
            if visitedIndex[i]:
                return
            visitedIndex[i] = True
            for p in ip[i]:
                if visitedPrime[p]:
                    continue
                visitedPrime[p] = True
                for j in pi[p]:
                    if visitedIndex[j]:
                        continue
                    dfs(j)

        def findPrimes(n):
            arr = [True] * (n + 1)
            p = 2
            while (p * p <= n):
                if arr[p]:
                    for i in range(p * p, n + 1, p):
                        arr[i] = False
                p += 1
            res = [p for p in range(2, n) if arr[p]]
            return res

        primes = findPrimes(max(nums))
        print(primes)

        # dict of index to prime and prime to index
        ip, pi = defaultdict(list), defaultdict(list) 

        for i, n in enumerate(nums):
            cur = n
            top = int(sqrt(n)) + 1
            for p in primes:
                if p > top:
                    break
                if cur % p == 0:
                    ip[i].append(p)
                    pi[p].append(i)
                while cur % p == 0:
                    cur //= p
            if cur > 1:
                ip[i].append(cur)
                pi[cur].append(i)
        
        visitedIndex = [False] * len(nums)
        visitedPrime = defaultdict(lambda: False)
        print(ip, pi)
        dfs(0)
        return all(visitedIndex)
