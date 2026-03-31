# Last updated: 3/31/2026, 5:28:40 AM
class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        i = 0
        while i < len(command):
            if command[i] == 'G':
                ans.append('G')
                i += 1
            elif command[i] == '(':
                if command[i + 1] == ')':
                    ans.append('o')
                    i += 2
                else:
                    # "(al)"
                    ans.append("al")
                    i += 4
            # Other cases are not possible
        return "".join(ans)