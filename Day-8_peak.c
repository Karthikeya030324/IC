#include <stdio.h>

int findPeakElement(int* nums, int numsSize);

int main() {
    int nums[] = {1, 3, 20, 4, 1, 0};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int peakIndex = findPeakElement(nums, numsSize);
    printf("Peak element found at index: %d\n", peakIndex);

    return 0;
}

int findPeakElement(int* nums, int numsSize) {
    if (numsSize == 1) {
        return 0; // Single element is always a peak
    }

    for (int i = 0; i < numsSize; i++) {
        if (i == 0) {
            if (nums[i] > nums[i + 1]) {
                return i;
            }
        } 
        else if (i == numsSize - 1) {
            if (nums[i] > nums[i - 1]) {
                return i;
            }
        } 
        else {
            if ((nums[i] > nums[i + 1]) && (nums[i] > nums[i - 1])) {
                return i;
            }
        }
    }
    return 0;
}
