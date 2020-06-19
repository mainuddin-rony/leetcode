class Solution:
    def intToRoman(self, num: int) -> str:
        lower_num_map = {
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX'
        }
        
        base_map = {
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        bases = list(base_map.keys())
        bases.sort(reverse=True)
        
        if num in lower_num_map.keys():
            return lower_num_map[num]
        if num in base_map.keys():
            return base_map[num]
        
        roman = ""
        
        print(bases)
        
        for base in bases:
            if num // base > 0:
                roman += base_map[base] * (num // base)
                rem_base = num - (base * (num // base)) 
                if rem_base in lower_num_map.keys():
                    roman += lower_num_map[rem_base]
                    return roman
                else:
                    num = rem_base
        return roman
        
                
