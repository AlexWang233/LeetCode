class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = [item for item in path.split('/') if item != '.' and item != '']
        stk = []
        for d in dirs:
            if d == '..':
                if len(stk) > 0:
                    stk.pop()
            else:
                    stk.append(d)

        return '/'+'/'.join(stk)