class Solution:
    def isPalindrome(self, x: int) -> bool:
        #(Current)Approach(New)
        #T(C(N)==O(N)) and S(C(N)==O(1)) as it requires non memory space allocation iteratively
        #storage usage(16.60mb and  min. runtime==45ms)
        if x<0 or (x!=0 and x%10==0):return False#Checking non decimal value
        h=0 #initalzing reverse val
        while x>h:#iterating both the left and right sub arrays
            h=h*10+x%10#reverseigng the digits
            x=x//10#dividning the output's decimal val
        return x==h or x==h//10#printing the both the original and reversed subarrys
