class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cur = i = 0
        l = len(sandwiches)
        q = deque(students)
        while cur < len(q):
            s = q.popleft()
            if sandwiches[i] == s:
                i += 1
                cur = 0
            else:
                q.append(s)
                cur += 1
        return len(q)