class Solution {
public:
    bool isPalindrome(int x) {
        //new_approach
        //optimal_sol(0ms) as it requires additional memory recurisvely
        if(x<0)return false;//Printing false to the initlaized (-ve) number
        int y=x;long rev=0;//Varibales declare and initlized
        while(y>0){//Positive Input Recursion
            rev=rev*10+y%10; y/=10;//reversing the Number I
            //x=rev;
            // y=rev;
        }return x==rev;}};//Assigning the Input to the reversed umber and printing it
        //old_Apporaches

    //     if(x<0 || x!=0 && x%10==0)return false;
    //     else return true;
    //     int h=0;
    //     while(x<=h){
    //         h=h*10+x%10;
    //         x=x/10;
        
    //     }x==h;return x || x==h/10;
    // }
