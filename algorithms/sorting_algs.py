# this code was created by Jacob Thom on November 8, 2021
# at current it implements:
# 	merge sort (admittedly done in an un-pythonic fashion)
# 	insertion sort
# 	bubble sort
# 	selection sort
# 	quicksort
# 	radix sort
#	bucket sort

#with plans for

# heap sort




import random

#first we need a function to get a randomized array of numbers of n size
def generate_random_array(n):
	arr = random.sample(range(1, n+1), n)
	return arr

def insertion_sort(arr):

	#for every element in the array
	for x in range(1, len(arr)):

		#keep track of current location. x-1 so that we work iteratively from front to back
		location = x-1
		#get the value of the current element
		key = arr[x]

		#while the current location has a greater value and we are not at the end of the array
		while (arr[location] > key and location >= 0):
			#shift everything down by 1 place
			arr[location + 1] = arr[location]
			#move the current location back by one
			location-=1
		#if we exit the loop we must be at the right spot, place the key/element
		arr[location+1] = key
	#yay, all done
	return arr


#this function merges two arrays back together in a sorted fashion. it looks very unpythonic but just defines things easier
def merge_sort_merge(arrA, arrB):
	#to keep track of locations in each array
	locationA = 0
	locationB = 0

	#easy length variables
	lenA = len(arrA)
	lenB = len(arrB)
	lenEnd = lenA + lenB

	#create a final arr
	end_arr = [0] * lenEnd
	location_end = 0

	#while neither list is at the end
	while locationA != lenA and locationB != lenB:
		#if current A is less than current B
		if arrA[locationA] <= arrB[locationB]:
			#place it in the array
			end_arr[location_end] = arrA[locationA]

			#increment location for A
			locationA+=1
		#B must be greater than A
		else: 
			#place current B into the array
			end_arr[location_end] = arrB[locationB]

			#increment location for A
			locationB+=1

		#increment the end array location
		location_end+=1
	#if we got to the end of A first
	if locationA == lenA:
		#while array not full
		while location_end != lenEnd:
			#keep progressing down both arrays
			end_arr[location_end] = arrB[locationB]
			locationB+=1
			location_end+=1
	#else we got the end of B first
	else:
		#while array not full
		while location_end != lenEnd:
			#keep progressing down both arrays
			end_arr[location_end] = arrA[locationA]
			locationA+=1
			location_end+=1

	return end_arr


#this function splits the array and then calls merge sort on each individual piece before merging them back together
def merge_sort(arr):
	i = len(arr)
	#if not at base case
	if i >= 3:
		
		midway_point = i//2

		#cut the array in half
		arrA = arr[0:midway_point]
		arrB = arr[midway_point:None]

		#split and then zip
		end_arr = merge_sort_merge(merge_sort(arrA), merge_sort(arrB))
	
	#we have reached the base case
	else:
		#if only one element
		if i == 1:
			#we want to return just that element in an array
			end_arr = arr
		#two elements
		else:
			#if out of order
			if arr[0] > arr[1]:
				#re arrange
				end_arr = [arr[1],arr[0]]
			else:
				#the array is fine
				end_arr = arr

	return end_arr

def bubble_sort(arr):
	lenA = len(arr)

	#for all elements
	for x in range(0, lenA):

		#last elements are already in order, -1 to account for end of array
		for i in range(0, lenA-x-1):

			#if two elements out of order
			if arr[i] > arr[i+1]:
				#swap
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
	return arr

def selection_sort(arr):
	lenA = len(arr)

	#for all elements
	for x in range(0, lenA):

		min_val = arr[x]
		min_index = x
		#first elements are already in order, -1 to account for end of array
		for i in range(x+1, lenA):
			#if the element is less than the min
			if arr[i] < min_val:
				#save it 
				min_val = arr[i]
				min_index = i
		
		#swap the resulting min with the first place in the sub array
		temp = arr[x]
		arr[x] = min_val
		arr[min_index] = temp

	return arr


#this function finds the best pivot/centre for sorting an array and preforms the sorting before and after the pivot point
def quick_sort_partition(arr, low, high):

	pivot = arr[high] #rightmost element will be placed at the correct spot

	index = low-1 # indicates lowest point of this partition which will be incremented to find the correct spot for the pivot

	#for every index in current partition
	for x in range(low, high):
		if arr[x] < pivot: # if element is less than the pivot i.e. that the element is correctly in position relative to the pivot
			index+=1 #move the soon to be pivot point forwards

			# swap the element of the index and of the current element
			temp = arr[index]
			arr[index] = arr[x]
			arr[x] = temp

	#swap the position to the right of our index position with our pivot point
	temp = arr[index+1]
	arr[index+1] = arr[high]
	arr[high] = temp

	return arr, index+1 #return arr and centre/pivot point


#this function splits the array and runs quicksort on both halves of the split array, each half of which has been semi-sorted by the partition function
def quick_sort_sort(arr, low, high):
	if low < high: # if not a single element
		arr, centre = quick_sort_partition(arr, low, high) # find a good partition point

		arr = quick_sort_sort(arr, low, centre - 1) # quicksort the first half
		arr =  quick_sort_sort(arr, centre+1, high) #quicksort the second half

	return arr # return arr

def quick_sort(arr):
	return quick_sort_sort(arr, 0, len(arr)-1)


def radix_sort(arr):

	max_digits = len(str(max(arr)))

	#for every digit available i.e. 100 has 3 digits...
	for digit in range (0, max_digits):

		#create 10 buckets for each possible digit 0-9
		buckets = [ [] for i in range(10)]

		#for each value in the array
		for x in arr:
			#get the bucket number by extracting that single digit
			to_be_bucket = (x// (10 ** digit)) % 10

			#add that value at the *end* of its proper bucket (i.e in order)
			buckets[to_be_bucket].append(x)

		#empty the original list
		del arr[:]

		#add the buckets in order to the end of the array
		for x in buckets:
			arr.extend(x)

	return arr


# tradional bucket sort is awful for arrays that are capped at an even power of 10 (unless you want to modify the code for 100 buckets) which can be done
# as seen below in a modified bucket sort
def bucket_sort(arr):

	fin_arr = []
	#find the largest digit
	largest_digit = len(str(max(arr))) -1

	#create 10 buckets for each possible digit 0-9
	buckets = [ [] for i in range(10)]

	#for every value in the array
	for x in arr:
		#get the bucket number by extracting the largest possible digit
		to_be_bucket = (x// (10 ** largest_digit)) % 10

		#add that value to the correct bucket
		buckets[to_be_bucket].append(x)

	#for every bucket
	for x in buckets:

		#because bucket sort is cheap, just sort the bucket with some random method. i chose quicksort because its simple, quick, and reliable
		fin_arr.extend(quick_sort(x))

	return fin_arr

#modified for more buckets (handles variable ranges better by defeating the pesky single multiple of 10)
def modified_bucket_sort(arr):

	fin_arr = []
	#find the largest digit and subtract 2 because we want the last 2 digits
	largest_digit = len(str(max(arr))) -3

	#create 101 buckets for each possible digit 0-100
	buckets = [ [] for i in range(101)]

	#for every value in the array
	for x in arr:
		#get the bucket number by extracting the largest possible digit
		to_be_bucket = x // (10**largest_digit)

		#add that value to the correct bucket
		buckets[to_be_bucket].append(x)

	#for every bucket
	for x in buckets:

		#because bucket sort is cheap, just sort the bucket with some random method. i chose quicksort because its simple, quick, and reliable
		fin_arr.extend(quick_sort(x))

	return fin_arr


def main():
	test = generate_random_array(1000)
	#print(test)

	print(bucket_sort(test))



if __name__ == "__main__":
	main()