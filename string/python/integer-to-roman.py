class Solution:
    def intToRoman(self, num: int) -> str:
        """LC 12. Integer to Roman

        """
        result = []
        symbol_val = [('M', 1000),('CM', 900),('D', 500),('CD', 400), ('C', 100),('XC', 90),\
            ('L', 50),('XL', 40),('X', 10),('IX', 9),('V', 5),('IV', 4),('I', 1)]
        
        for symbol, v in symbol_val:
            count = num // v
            num %= v
            if count > 0:
                result.append(symbol*count)
        return "".join(result)
        