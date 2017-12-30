int removeDuplicates(int *nums, int numsSize){
	int leap = 0, test, move;

	for(int i = 0; i < numsSize - 1; i++){
		if(nums[i] == nums[i + 1]){

			for(test = i; test < numsSize - 1; test++){
				if(nums[test] == nums[test + 1])
					leap++;
				else
				    break;
			}

			for(move = i + 1; move < numsSize - leap; move++){
				nums[move] = nums[move + leap];
			}

			numsSize -= leap;
			leap = 0;
		}
	}

	return numsSize;
}