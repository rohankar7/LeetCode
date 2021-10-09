//In-> An array of increasingly sorted ints;
//Out-> The total no. of non-duplicates from index 0;
import java.util.Arrays;
class RemoveDuplicatesFromArray{
    public int removeDuplicates(int[] nums) {
        if(nums.length==0)
            return 0;
        int replacement = nums[0];
        int count = 0;
        for(int i=1;i<nums.length;i++){
            if(nums[i]==replacement){
                nums[i] = nums[nums.length - 1] + 1;
                ++count;
            }
            else{
                replacement = nums[i];
            }
        }
        int k = nums.length - count;
        Arrays.sort(nums);
        return k;
    }
}