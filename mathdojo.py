



class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        # your code here
        self.result += num
        if len(nums) > 0:
            for i in range(len(nums)):
                self.result += nums[i]
        return self
    def subtract(self, num, *nums):
        self.result -= num
        if len(nums) > 0:
            for i in range(len(nums)):
                self.result -= nums[i]
        return self
# create an instance:
md = MathDojo()
# to test:
y = md.add(5).add(2,3,6,8).add(12,4,40)
z = md.subtract(14,4,1).subtract(11,4).subtract(9,5,6)


x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!












