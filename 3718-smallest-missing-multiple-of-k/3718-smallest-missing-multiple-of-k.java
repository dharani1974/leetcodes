class Solution {
    public int missingMultiple(int[] nums, int k) {
        if (nums.length==1){
            if (nums[0]==k){
                return k+k;
            }
            else {
                return k;
            }
        }
        int min =k;
        Arrays.sort(nums);
        int i=0;
        while (i<nums.length){
            if (nums[i]<min){
                i++;
            }
            else if(nums[i]==min){
                min+=k;
                i++;
            }
            else{
                return min;
            }
        }
        return min;
    }
}