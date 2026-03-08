class Solution(object):
    def romanToInt(self, s):
        value_symbol=[
        (1000, "M"),   
        (900,  "CM"),  
        (500,  "D"),   
        (400,  "CD"),  
        (100,  "C"),   
        (90,   "XC"), 
        (50,   "L"),  
        (40,   "XL"),  
        (10,   "X"),  
        (9,    "IX"),  
        (5,    "V"),   
        (4,    "IV"),  
        (1,    "I")    ]
        nums=0
        i=0
        while i<len(s):
            for value , symbol in value_symbol:
                if s[i:i+len(symbol)]==symbol:
                    nums+=value
                    i+=len(symbol)
                    break

        return nums
