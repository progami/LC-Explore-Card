class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        sum = 0
        length = len(digits)

        for i in range(length):
            
            power_factor = (10**(length-1-i))
            place = digits[i] * power_factor             
            sum += place
       
        sum += 1

        places = 0
        temp_sum = sum
        
        while temp_sum:

            temp_sum = temp_sum // 10
            places += 1

        print('places: {}'.format(places))

        digits_plus_one = []
        j = 0

        while places-1-j >= 0:
            
            print(sum)
            power_factor = 10 ** (places-1-j)
            digit = sum // power_factor
            digits_plus_one.append(digit)
            sum -= digit * power_factor

            j += 1

        return digits_plus_one


# print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([9]))
