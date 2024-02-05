class Solution:
    def isPalindrome(self, x: int) -> bool:
        #new_Approach
        #storage usage(16.60mb and  min. runtime==45ms)
        if x<0 or (x!=0 and x%10==0):return False#Checking non decimal value
        h=0 #initalzing reverse val
        while x>h:#iterating both the left and right sub arrays
            h=h*10+x%10#reverseigng the digits
            x=x//10#dividning the output's decimal val
        return x==h or x==h//10#printing the both the original and reversed subarrys

        #old_approach(best_case(S(c(n)=O(n)))
       # s=str(x);t=str()
        #for i in range(len(s)):
            #for j in range(i-1,len(s)):
               # if s[j]==s[i]:return True#s[i]=s[j];s[j]=t;
                #elif s[i]=='-' and s[j]=='-':return False
                #elif s[i]>s[j] or s[j]>s[i] :return False
                
        #if x<0:return False
        #elif x==0:return True
        #else :return False
        #num=0;rev=0
        #while x>0:ls=x%10;rev=rev*10+ls;x=x//10
        #return num==rev
