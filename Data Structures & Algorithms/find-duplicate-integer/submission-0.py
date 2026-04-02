class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        '''
        array will have alwasy 1 to n  but the lenght is n+1
        which means duplciates exist hence there is a cycle
        how do we dectect cylce slow fast ptr
        and then detect the head of the cycel which is the repeate item
        cux it will have 2 incoming edges type shii
        '''
        while True:
            slow =  nums[slow] # go once
            fast = nums[nums[fast]] # go twice
            # eventuallly they collide and hence duplcate exist
            if slow == fast:
                break
        # now from slow to head of cycle the path =  from start to head of cycle
        # when they collide thats the duplcated item
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow
        

        