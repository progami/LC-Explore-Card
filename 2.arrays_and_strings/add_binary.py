class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        max_len = max(len(a), len(b))
        result = ''
        carry = 0
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        # Iterating from right to left
        for i in range(max_len - 1, -1, -1):

            sum = int(a[i]) + int(b[i]) + carry
            result = str(sum % 2) + result
            carry = sum // 2

        # If there's a carry left, add it to the result
        if carry != 0:
            result = str(carry) + result

        return result

print(Solution().addBinary('100', '10'))  # Output: "110"

