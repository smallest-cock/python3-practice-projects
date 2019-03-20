# Takes input of 10 integers. Adds them and prints the result.

total = 0
nums = []
nums.append(int(input('Enter an integer:  ')))
for i in range(9):
    nums.append(int(input('Enter another integer:  ')))
for i in range(len(nums) - 1):
    total += nums[i]
    print(str(nums[i]), end='+')
print(str(nums[-1]) + ' = ' + str(total))
