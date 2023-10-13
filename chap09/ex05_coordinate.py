def mergeSort(l, left, right):
    center = (left + right) // 2
    if left < right:
        mergeSort(l, left, center)
        mergeSort(l, center+1, right)
        merge(l, left, center + 1, right)

def merge(l, left, right, rightEnd):
    start = left
    leftEnd = right - 1
    result = []
    while left <= leftEnd and right <= rightEnd:
        if l[left][0] < l[right][0]:
            result.append(l[left])
            left += 1
        else:
            result.append(l[right])
            right += 1
    while left <= leftEnd:
        result.append(l[left])
        left += 1
    while right <= rightEnd:
        result.append(l[right])
        right += 1

    for ele in result:
        l[start] = ele
        start += 1
        if start > rightEnd:
            break

input_list = input("input : ").split()
input_list = [int(x) for x in input_list]
paired = []
bus = []
count = 0
for i in input_list:
    bus.append(i)
    count += 1
    if count == 2:
        paired.append(bus)
        bus = []
        count = 0

mergeSort(paired, 0, len(paired)-1)

store = []

for i in range(len(paired)):
    for j in range(i):
        if paired[i][0] > paired[j][0]:
            if paired[i][1] < paired[j][1]:
                store.append(int(paired[i][0]))
                store.append(int(paired[j][0]))

print(f"ans = {sum(store)}")
