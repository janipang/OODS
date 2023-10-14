datas = [list(map(int, num.split())) for num in input("Enter Input : ").split('/')]
thing, box = datas[0], datas[1][0]
weight = 0

def min_weight(thing, box):
    capacity = max(thing)
    while capacity <= sum(thing):
        getbox = 0
        for i in range(box):
            set = []
            while (getbox < len(thing)) and (sum(set) + thing[getbox] <= capacity):
                set.append(thing[getbox])
                getbox += 1
        if getbox == len(thing):
            return capacity
        capacity += 1

print(f"Minimum weigth for {box} box(es) = {min_weight(thing, box)}")