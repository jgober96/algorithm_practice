#!/usr/bin/python
# Uses python3
import sys
# Naive solution
# Traverse through all pariwise values, finding maximum sum value and returning that
# Complexity - O(n2)

# better solution
# Go through all numbers keeping track of the max and its index; go through again and find all BUT the one max

# best ? 
# go through once, keeping 2 numbers aside and only replacing them when greater numbers are there

input = sys.stdin.read();
split_input = input.split()
converted_input = list(map(lambda x: int(x), split_input))

## O(2n)
def max_pairwise_product(length, values):

	# initialize value and max index vars
	max_val = 0;
	second_max_val = 0;
	max_index = 0;

	# Get maximum value
	for i in range(length):
		if values[i] > max_val:
			max_val = values[i];
			max_index = i;

	# Get second largest value
	for i in range(length):
		if i != max_index:
			if values[i] > second_max_val:
				second_max_val = values[i];

	# product of two largest					
	return max_val * second_max_val;

## O(n)
def max_pairwise_product_optimized(length, values):
	
	# get frist pair of nums
	max_nums = [values[0], values[1]];
	if (max_nums[0] > max_nums[1]):
		max_nums = [values[1], values[0]];

	for i in range(2, length):
		curr_val = values[i];
		if curr_val > max_nums[0]:
			if curr_val >= max_nums[1]:
				max_nums[0] = max_nums[1];
				max_nums[1] = curr_val
			else:
				max_nums[0] = curr_val
	return max_nums[0] * max_nums[1]



print(max_pairwise_product_optimized(converted_input[0], converted_input[1:]));
