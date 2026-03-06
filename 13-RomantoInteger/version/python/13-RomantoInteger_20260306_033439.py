# Last updated: 3/6/2026, 3:34:39 AM
class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        roman = {
            "I" : 1,
            "IV" : 4,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "XC" : 90,
            "C" : 100,
            "D" : 500,
            "CM " :900,
            "M" : 1000
        }
        roman_to_integer = 0
        i = 0
    
        for i in range(n):
            if i<n-1 and roman[s[i]] < roman[s[i+1]] :
                roman_to_integer -= roman[s[i]]
            else:
                roman_to_integer += roman[s[i]]
        return roman_to_integer