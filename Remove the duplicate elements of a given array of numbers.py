Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def remove_duplicates(nums):
...     for i in range (len(nums)-1, 0, -1):
...         if nums[i] == nums[i-1]:
...             del nums[i-1]
...     return len(nums)
... 
... print(remove_duplicates([0,0,1,1,2,2,3,3,4,4,4]))
... print(remove_duplicates([1, 2, 2, 3, 4, 4]))
