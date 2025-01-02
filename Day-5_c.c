/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** fizzBuzz(int n, int* returnSize) {
    char** arr=malloc(n* sizeof(char*));
    * returnSize = n; 
    int i;
    for (i=1;i<=n;i++)
    {
        if((i%3==0) && (i%5==0))
        {
            arr[i-1]=strdup("FizzBuzz");
        }
        else if(i%3==0)
        {
            arr[i-1]=strdup("Fizz");
        }
        else if(i%5==0)
        {
            arr[i-1]=strdup("Buzz");
        }
        else
        {
            arr[i-1] = malloc(12 * sizeof(char));
            sprintf(arr[i - 1], "%d", i);
        }
    }
    return arr;
}