def bubbleSort(array):
	if len(array) == 1:
		return array
	if array[1] < array[0]:
		array[0], array[1] = array[1], array[0]
	sorted_array = bubbleSort(array[1:])
	sorted_array.insert(0, array[0])
	return sorted_array

def outerBubbleSort(array):
	if len(array) == 1:
		return array
	array = bubbleSort(array)
	sorted = outerBubbleSort(array[:len(array) - 1])
	sorted.append(array[len(array) - 1])
	return sorted

#source = https://www.geeksforgeeks.org/bubble-sort/
nums = [int(i) for i in input("Enter Input : ").split()]
print(outerBubbleSort(nums))


