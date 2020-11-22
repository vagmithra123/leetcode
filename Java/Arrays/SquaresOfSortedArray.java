class Solution {
    public int[] sortedSquares(int[] A) {
        int[] res = new int[A.length];
        int n = A.length ;
        int i =0; int j = n -1; 
        for(int pos = n-1; pos >= 0; pos--){
            if(Math.abs(A[i]) > Math.abs(A[j])){
                res[pos] = A[i] * A[i];
                i++;
            }else{
                res[pos] = A[j] * A[j];
                j--;
            }
        }
      return res;  
        
    }
}