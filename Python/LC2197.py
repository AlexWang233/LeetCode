class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        dq = deque([])
        for n in nums:
            dq.append(n)
            while len(dq) >= 2:
                n1 = dq.pop()
                n2 = dq.pop()
                n3 = gcd(n1, n2)
                if n3 == 1:
                    dq.append(n2)
                    dq.append(n1)
                    break
                n1 *= (n2 // n3)
                dq.append(n1)
        return list(dq)