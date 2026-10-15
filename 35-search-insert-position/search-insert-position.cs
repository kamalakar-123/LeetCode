public class Solution {
    public int SearchInsert(int[] nums, int target) {
        int length = nums.Length;
        for (int i = 0; i < length; i++) {
            if (nums[i] >= target) {
                return i;
            }
        }
        return length;
    }
}