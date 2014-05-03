__author__ = 'g42gregory'
max = 1000
nums = set()

#go though 3s
x = 1
while 3 * x < max:
    nums.add(3 * x)
    x += 1

#go though 5s
x = 1
while 5 * x < max:
    nums.add(5 * x)
    x += 1

sum = 0
for num in nums:
    sum = sum + num

print sum