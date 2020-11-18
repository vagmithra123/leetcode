class LongestSubstringWithoutRepeatingChars {
    public int lengthOfLongestSubstring(String s) {
     int maxLen = 0;
     int left = 0; int right = 0;
        HashSet<Character> set = new HashSet<Character>();
        while(right < s.length()){
            while(set.contains(s.charAt(right))){
                set.remove(s.charAt(left++));
            }
            set.add(s.charAt(right++));
            maxLen = Math.max(maxLen, right -left);
        }
        
       return maxLen; 
    }

   
}