class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_first = -1
        s = str(num)
        for c in s:
            n = int(c)
            if n != 9:
                max_first = n
                break

        max_num = 0
        if max_first == -1:
            max_num = num

        min_first = -1
        for c in s:
            n = int(c)
            if n != 0:
                min_first = n
                break

        min_num = 0
        if min_first == -1:
            min_num = num

        max_s = ""
        min_s = ""
        for c in s:
            n = int(c)
            if n == max_first:
                max_s += "9"
            else:
                max_s += c
            if n == min_first:
                min_s += "0"
            else:
                min_s += c

        return int(max_s) - int(min_s)

