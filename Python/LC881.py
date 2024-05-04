class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        j = 1
        r = len(people) - 1
        l = 0
        count = 0
        while r >= l:
            if people[r] + people[l] <= limit:
                l += 1
            r -= 1
            count += 1
        return count