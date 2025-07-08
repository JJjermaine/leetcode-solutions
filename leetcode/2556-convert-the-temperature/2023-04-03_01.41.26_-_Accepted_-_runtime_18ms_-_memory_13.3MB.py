class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        a = []
        k = celsius + 273.15
        f = celsius * 1.8 + 32
        a.append(k)
        a.append(f)
        return a