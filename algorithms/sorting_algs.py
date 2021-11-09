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

def main():
	test = generate_random_array(100)
	print(merge_sort(test))

if __name__ == "__main__":
	main()