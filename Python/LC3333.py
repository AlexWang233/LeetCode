class Solution:
    MOD = 10**9 + 7

    def possibleStringCount(self, word: str, k: int) -> int:
        if not word:
            return 0

        groups = []
        count = 1
        for i in range(1, len(word)):
            # count lengths of each group of consecutive identical letters
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        # calculate total number of original strings (of any length)
        total = 1
        for num in groups:
            total = (total * num) % self.MOD

        # if shortest original string has length >= k, short circuit
        if k <= len(groups):
            return total

        # dp[i] represents the number of original strings of length i
        dp = [0] * k
        dp[0] = 1

        for num in groups:
            # new_dp[i] represent number of strings of length i with current group
            # dp[i] represents number of strings of length i w/o current group
            new_dp = [0] * k
            sum_val = 0
            for s in range(1, k):
                # append a character from current group can make a string of length i
                # add from dp[s-1] not dp[s] bc we need at least 1 from current group
                new_dp[s] = new_dp[s - 1] + dp[s - 1]
                # if current group doesn't have enough, check how many strings of length s-num
                # with only 1 character from current group and deduct
                # this is same as # of strings so far w/ all characters from current group
                if s > num:
                    new_dp[s] += (self.MOD - dp[s - 1 - num])
                new_dp[s] %= self.MOD
            dp = new_dp

        # start counting from len(groups) bc we need at least 1 char from each group
        invalid = sum(dp[len(groups):k]) % self.MOD
        return (total - invalid + self.MOD) % self.MOD