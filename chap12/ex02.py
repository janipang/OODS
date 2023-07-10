print(" *** Rank score ***")
src = list(map(str, input("Enter ID and Score end with ID : ").split()))
the_id = int(src.pop(-1))
print(src)
print(the_id)

dict_src = {}
for i in range(int(len(src)/2)):
    dict_src[str(src[2*i])] = float(src[(2*i + 1)])
sorted_dict = dict(sorted(dict_src.items(), key=lambda x: x[1], reverse = True))
print(dict_src)
# print((sorted_dict))

flipped = {}
 
for key, value in sorted_dict.items():
    if value not in flipped:
        flipped[value] = [int(key)]
    else:
        flipped[value].append(int(key))
# print(flipped)
rank = 0
for key, value in flipped.items():
    if len(value) == 1:
        rank += 1
    if (len(value) == 1 and value[0] == the_id):
        print(rank)
        exit
    if (len(value) > 1 and the_id not in value):
        rank += len(value)
    if (len(value) > 1 and the_id in value):
        for mini_val in value:
            if mini_val <= the_id:
                rank += 1
        print(rank)
        exit
