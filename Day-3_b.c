char * mergeAlternately(char * word1, char * word2){
    int i=0,j=0,k=0;
    int w1=strlen(word1);
    int w2=strlen(word2);
    int n=w1+w2+1;
    char * word3=(char *)malloc(n * sizeof(char));
    while(w1!=0 && w2!=0)
    {

        if(k%2==0)
        {
            word3[k]=word1[i];
            i++;w1--;k++;
        }
        else
        {
            word3[k]=word2[j];
            j++;w2--;k++;
        }
    }
    while(w1>0)
    {
        word3[k]=word1[i];
        i++;w1--;k++;
    }
    while(w2>0)
    {
        word3[k]=word2[j];
        j++;w2--;k++;
    }
    word3[k] = '\0'; 
    return word3;
}