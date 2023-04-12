class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        ps = path.split('/')
        for s in ps:
            if s == '.' or s == '':
                continue
            elif s == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(s)
        return '/' + '/'.join(stk)