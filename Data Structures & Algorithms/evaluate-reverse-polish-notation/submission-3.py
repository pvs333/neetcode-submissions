class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        res = 0
        while tokens:
            x = tokens.pop(0)
            if x.isdigit():
                nums.append(int(x))
            elif x[0] == "-" and x[1:].isdigit():
                nums.append(int(x))

            else:
                if x == "+":
                    a = nums.pop()
                    b = nums.pop()
                    nums.append(a+b)
                elif x == "-":
                    a = nums.pop()
                    b = nums.pop()
                    nums.append(b-a)
                elif x == "*":
                    a = nums.pop()
                    b = nums.pop()
                    nums.append(a*b)
                elif x == "/":
                    a = nums.pop()
                    b = nums.pop()
                    nums.append(int(b/a))
        return nums[0]


            