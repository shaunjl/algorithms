"""
Leetcode 78. Subsets

Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Solution:
Use recursion with backtracking.
Backtracking is basically where you run the search with some info, step back, and run it with a one step back
The basic idea is that to find all subsets you consider that each element can either be included or not included.
So we run a recursion like this:

Input: [1,2,3]

                                 start
(decision to add 1)           /         \
                           [1]            []
(...to add 2)           /       |        / \
                   [1,2]         [1]      ...
(...to add 3)     /     |       /   \
            [1,2,3]    [1,2] [1,3]   [1]


all the leaf nodes are our subsets
"""

def subsets(arr: list[int]) -> list[int]:
	ans = []

	subset = []
	def dfs(start_index: int):
		if start_index >= len(arr):
			ans.append(subset.copy())
			return

		# use the option where you add it to the list
		subset.append(arr[start_index])
		dfs(start_index + 1)

		# now BACKTRACK
		subset.pop()
		dfs(start_index + 1)

	dfs(0)

	return ans


print(subsets([1,2,3]))