import numpy as np
a = int(input("enter the length of an array"))
ar = []
for i in range(a):
    ar.append(input())
nums = np.array(ar)
print("Original array:")
print(nums)
p = 5
new_nums = np.zeros(len(nums) + (len(nums)-1)*(p))
new_nums[::p+1] = nums
print("\nNew array:")
print(new_nums)