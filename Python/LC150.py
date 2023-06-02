class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        v = "+-*/"
        for token in tokens:
            if not token in v:
                s.append(int(token))
            else:
                if token == '+':
                    s.append(s.pop() +  s.pop())
                elif token == '-':
                    s.append(-s.pop() +  s.pop())
                elif token == '*':
                    s.append(s.pop() *  s.pop())
                else:
                    t = (s.pop(-2) / s.pop())
                    if t > 0:
                        t = math.floor(t)
                    else:
                        t = math.ceil(t)
                    s.append(t)
        return s[-1]