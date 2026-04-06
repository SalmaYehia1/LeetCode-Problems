# Last updated: 4/6/2026, 10:26:59 PM
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')
      


        