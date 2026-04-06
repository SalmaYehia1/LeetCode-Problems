# Last updated: 4/6/2026, 10:26:40 PM
class Solution(object):
    def convertTemperature(self, celsius):
        res=[]
        res.append(celsius + 273.15)
        res.append(celsius * 1.80 + 32.00)
        return res