class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry = len(a) - 1, len(b) - 1, 0
        ans = ""
        while i >= 0 or j >= 0:
            n = carry
            if i >= 0:
                n += int(a[i])
                i -= 1
            if j >= 0:
                n += int(b[j])
                j -= 1
            carry = int(n / 2)
            ans += str(n % 2)
            
        if carry:
            ans += str(carry)
            
        return ans[::-1]