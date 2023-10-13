datas = [data.split() for data in input("input : ").split(',')]
row, column = int(datas[0][0]), int(datas[0][1])
datas[1] = [int(num) for num in datas[1]]
table = [ [0]*column for i in range(row)]
least = min(datas[1])
cox = (datas[1].index(least))//column

for i in range(row):
    for j in range(column):
        table[i][j] = int(datas[1][(i*row)+j])
    # print(table[i])
most1 = max(table[cox])
coy = table[cox].index(most1)

most2 = 0
for i in range(row):
    for j in range(column):
        if (j == coy and table[i][j] > most2):
            most2 = table[i][j]
        
# print(least , cox)
# print(most1 , coy)
print(most2)