num = input()
nums = num.split( )
result = []
for i in range(len(nums)):
    a = nums[i][::-1]
    result.append(a)
print(max(result))