// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

// Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

class Solution {
    public void sortColors(int[] nums) {
        for(int i =0; i< nums.length -1 ; i++){
            for(int j = i +1; j< nums.length ; j++){
                if(nums[i] > nums[j]){
                    int tmp  =0;
                    tmp = nums[j];
                    nums[j] = nums[i];
                    nums[i] = tmp;
                }else{
                    continue;
                }
            }
        }
    }
}