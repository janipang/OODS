def selectionSort(array, placed=[]):
    if len(array) == 1:
        return array
    max_index = find_max(array)
    if max_index != len(array) - 1:
        array[len(array) - 1], array[max_index] = array[max_index], array[len(array) - 1]
        fullarray = array + placed
        print(f"swap {array[max_index]} <-> {array[len(array) - 1]} : {fullarray}")
    placed.insert(0, array[len(array) - 1])
    sorted_array = selectionSort(array[:len(array) - 1],placed)
    sorted_array.append(array[len(array) - 1])
    return sorted_array
    
def find_max(array, index=0):
    if index >= len(array):
        return len(array) - 1
    if array[index] >= array[find_max(array, index+1)]:
        return index
    return find_max(array, index+1)
    
# source = https://www.geeksforgeeks.org/selection-sort/
nums = [int(i) for i in input("Enter Input : ").split()]
print(selectionSort(nums))