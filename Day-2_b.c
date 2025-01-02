int removeElement(int* nums, int numsSize, int val) {
    int n=numsSize;
    int pos;
    int j=0;
    int x=val;
    for(int i=0;i<n;i++)
    {
        if(nums[i]!=x)
        {
            nums[j]=nums[i];
            j++;
        }
    }
    return j;
}