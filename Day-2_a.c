int removeDuplicates(int* nums, int numsSize) {
    int n=numsSize;
    int j=0;
    for(int i=0;i<n-1;i++)
    {
        if(nums[i]!=nums[i+1])
        {
            nums[j]=nums[i];
            j++;
        }
    }
    nums[j++] = nums[n-1];
    return j;
}