class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # all bits a OR b differ from c require 1 flip
        f1 = (a | b) ^ c
        # all bits for which a AND b differ from f1 require 1 more flip
        # since this means that it is 1 in a and b but 0 in c
        f2 = (a & b & f1)
        return f1.bit_count() + f2.bit_count()