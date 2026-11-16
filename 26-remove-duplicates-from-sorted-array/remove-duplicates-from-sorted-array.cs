public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int n = nums.Length;
        if(n==1){
            return 1;
        }
        int i=0;
        int j=1;
        while(j<n){
            if(nums[j]!=nums[i]){
                i++;
                int temp=nums[i];
                nums[i]=nums[j];
                nums[j]=temp;

            }
            j++;
        }
        return i+1;
        
    }
}