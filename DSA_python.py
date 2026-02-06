#TWO SUM
'''class Solution(object):
    def twoSum(self, nums, target):
       mpp = {}
       for i in range(len(nums)):
            need = target - nums[i]
            if need in mpp:
                return [mpp[need],i]
            mpp[nums[i]] = i
        '''

#CONTAINS DUPLICATE
'''class Solution(object):
    def containsDuplicate(self, nums):
        st = set()
        for i in range(len(nums)):
            if nums[i] in st:
                return True
            st.add(nums[i])
        return False
        '''

#BEST TIME TO BUY AND SELL STOCK
'''class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        mini = prices[0]
        for i in range(len(prices)):
            currProfit = prices[i] - mini
            maxProfit = max(maxProfit,currProfit)
            mini = min(mini,prices[i])
        return maxProfit'''

#VALID ANAGRAM
'''class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        freq = [0]*26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1
            if(freq[ord(ch) - ord('a')] < 0):
                return False
        return True'''

#VALID PARENTHESES
'''class Solution(object):
    def isValid(self, s):
        st = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                st.append(ch)
            else:
                if not st:
                    return False
                if (ch == ')' and st[-1] == '(') or (ch == ']' and st[-1] == '[') or (ch == '}' and st[-1] == '{') :
                    st.pop()
                else:
                    return False

        return len(st) == 0
        '''

#PRODUCT OF ARRAY EXCEPT SELF
'''class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1]*n
        for i in range(1,n):
            res[i] = res[i-1]*nums[i-1]
        suffix = 1
        for i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
        '''

#MAXIMUM SUBARRAY
'''class Solution(object):
    def maxSubArray(self, nums):
        maxi = -1e9
        sum = 0
        for num in nums:
            if sum < 0:
                sum = 0
            sum += num
            maxi = max(maxi,sum)
        return maxi
'''
#3SUM
'''class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1
            while j<k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -=1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res
        '''

#MERGE INTERVALS
'''class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda x:x[0])
        merged = []
        temp = intervals[0]
        for i in range (1,len(intervals)):
            if intervals[i][0] <= temp[1]:
                temp[1] = max(temp[1],intervals[i][1])
            else:
                merged.append(temp)
                temp = intervals[i]
        merged.append(temp)
        return merged'''

#REVERSE LINKED LIST
'''# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        temp = head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
        '''

#DETECT CYCLE IN A LINKED LIST
'''# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False'''

#FIND MINIMUM IN ROTATED SORTED ARRAY
'''class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        left = 0
        right = n-1
        ans = float('inf')
        while left <= right:
            mid = left + (right-left)//2
            if nums[left] <= nums[mid]:
                ans = min(ans,nums[left])
                left = mid+1
            else:
                ans = min(ans,nums[mid])
                right = mid-1
        return ans'''

#NO OF ISLANDS
'''class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid,i,j)
        return count

    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return 
        grid[i][j] = '#'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)'''
# longest repeating character repalcement
'''class Solution(object):
    def characterReplacement(self, s, k):
        n = len(s)
        left = 0
        right = 0
        hash = [0] * 26
        maxi = 0
        ans = 0

        while right < n:
            hash[ord(s[right]) - ord('A')] += 1
            maxi = max(maxi, hash[ord(s[right]) - ord('A')])

            # Shrink window if more than k replacements needed
            while (right - left + 1) - maxi > k:
                hash[ord(s[left]) - ord('A')] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans'''
