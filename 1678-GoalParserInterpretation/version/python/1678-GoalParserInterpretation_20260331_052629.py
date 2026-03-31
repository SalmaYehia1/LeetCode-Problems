# Last updated: 3/31/2026, 5:26:29 AM
1class Solution:
2    def interpret(self, command: str) -> str:
3        s=command.replace('()','o')
4        s=s.replace('(al)','al')
5        return s
6
7
8        