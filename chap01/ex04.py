#Chapter : 1 - item : 4 - สนุกไปกับการวาดรูป (2)

print("*** Fun with Drawing ***")
py_wid = int(input("Enter input : "))
sq_wid = ((4 * py_wid) - 3)
for i in range(sq_wid):
    for j in range(sq_wid):
        if (i < (sq_wid // 2) + 1):
            if j % 2 == 0 and (j <= i or j >= sq_wid - 1 - i): 
                print('#', end = '')
            elif i % 2 == 0 and (j >= i and j <= sq_wid - 1 - i):
                print('#', end = '')
            else:
                print('.', end = '')
        else:
            if j % 2 == 0 and (j <= sq_wid - 1 - i or j >= i):
                print('#', end = '')
            elif i % 2 == 0 and (j >= sq_wid - 1 - i and j <= i):
                print('#', end = '')
            else:
                print('.', end = '')
    print('\n', end = '')