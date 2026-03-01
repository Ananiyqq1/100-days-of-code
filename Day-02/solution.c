int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int count=0; 
    int max_count = 0;
    
    for(int i = 0; i < numsSize; i++){
        if (nums[i] == 1){
            count++;
        if (count > max_count){
        max_count = count;}    
       }else{
            count = 0;
        }
    }
    return max_count;
}