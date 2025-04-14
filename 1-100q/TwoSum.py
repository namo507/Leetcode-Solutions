'''
	Given an array of integers, return indices of the two numbers such that they add up to a specific target.

	You may assume that each input would have exactly one solution, and you may not use the same element twice.

	Example:

	Given nums = [2, 7, 11, 15], target = 9,

	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
'''

class Solution(object):
	def twoSum(self, nums, target):
		mapping = {}

		for index, val in enumerate(nums):
			diff = target - val
			if diff in mapping:
				return [index, mapping[diff]]
			else:
				mapping[val] = index

# Space: O(N)
# Time: O(N)

'''
Code Explanation

class Solution(object):: This defines a class named Solution. In many coding platforms (like LeetCode), you're expected to define your solution within a class. The object is there for inheritance, making Solution a standard Python object.

def twoSum(self, nums, target):: This defines the twoSum method within the Solution class. It takes two arguments:

nums: A list of integers.
target: The target sum.
mapping = {}: This initializes an empty dictionary called mapping. This dictionary will be used to store each number in nums along with its index. It serves as a hash table for quick lookups.

for index, val in enumerate(nums):: This loop iterates through the nums list. enumerate is a built-in Python function that returns both the index and the value of each element in the list.

diff = target - val: Inside the loop, this calculates the difference (diff) between the target and the current value (val). This diff is the number we need to find in the rest of the array to achieve the target sum.

if diff in mapping:: This checks if the diff is already a key in the mapping dictionary. If it is, it means we've already encountered a number that, when added to the current number (val), equals the target.

return [index, mapping[diff]]: If the diff is found in the mapping, this line returns a list containing the current index and the index of the diff (which was stored in the mapping dictionary earlier). This is the solution!

else: mapping[val] = index: If the diff is not in the mapping, it means we haven't yet found a number that, when added to the current number, equals the target. So, we store the current number (val) and its index in the mapping dictionary. This way, if we encounter its complement later, we can quickly find its index.

Time and Space Complexity

Time Complexity: O(N) - The code iterates through the nums list once. Dictionary lookups (if diff in mapping:) take O(1) time on average.
Space Complexity: O(N) - In the worst case, the mapping dictionary might store all the elements of the nums list.
Example

Let's trace the example nums = [2, 7, 11, 15], target = 9:'
'mapping = {}
Loop iteration 1: index = 0, val = 2, diff = 9 - 2 = 7. 7 not in mapping. mapping[2] = 0. mapping is now {2: 0}.
Loop iteration 2: index = 1, val = 7, diff = 9 - 7 = 2. 2 in mapping!
return [1, mapping[2]] which is [1, 0].
The function correctly returns [1, 0] because nums[1] + nums[0] = 7 + 2 = 9.

'''
