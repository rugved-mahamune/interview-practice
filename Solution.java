class Solution {
    public static int longestPalindrome(String s) {
        if(s == null || s.length() < 1) return 0;
        int left = 0;
        int right = 0;
        
        for(int i=0;i<s.length();i++){
            int len1 = expandPalindrome(s,i,i);
            int len2 = expandPalindrome(s,i,i+1);
            int len = Math.max(len1,len2);
            System.out.printf("left: %d, right:%d, len1:%d, len2:%d, i:%d",left,right,len1,len2,i);
            System.out.println("");
            if(len > right - left){
                left = i - ((len-1)/2);
                right = i+ (len/2);
            }
            
        }
        System.out.println(s.substring(left,right+1));
        return s.substring(left,right+1).length();
    }
    
    private static int expandPalindrome(String s, int left, int right){
        if(left>right) return 0;
        
        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
            left--;
            right++;
        }
        int ans = right -left-1;
        //System.out.println(right + " "+left + "Ans"+ ans);
        return right-left-1;
    }
    public static void main(String args[]){
        longestPalindrome("abcdefe");
    }
}