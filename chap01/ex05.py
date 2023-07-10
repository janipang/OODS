print("*** Fun with countdown ***")
train = list(map(int, input("Enter List : ").split(' ')))

i = -1
mini_train = []
all_count = []
result = []
def count_down(i):
    global mini_train, all_count, train
    if (i < -len(train)):
        return 0
    
    now_num = train[i]

    if (now_num == count_down(i - 1) - 1):
        mini_train.append(train[i - 1])
    else:
        mini_train = []
    if (now_num == 1):
        mini_train.append(now_num)
        all_count.append(mini_train)
        # print(mini_train)
        mini_train = []
    return now_num

count_down(i)
result.append(len(all_count))
result.append(all_count)
print(result)
