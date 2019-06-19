class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack, base = [], {'', '.', '..'}
        # for p in path.split('/'):
        #     if p in base:
        #         if p == '..' and stack:
        #             stack.pop(-1)
        #     else: stack.append(p)
        # return '/' + '/'.join(stack)
        stack = []
        for p in path.split('/'):
            if p is '' or p is '.':
                continue
            if p == '..':
                if stack:
                    stack.pop(-1)
            else:
                stack.append(p)
        return '/' + '/'.join(stack)


s = Solution()
print(s.simplifyPath("/a/./b/../../c/"))
print(s.simplifyPath("/a/../../b/../c//.//"))
print(s.simplifyPath("/a//b////c/d//././/.."))
