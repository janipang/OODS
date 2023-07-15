    
def range(start, stop = None, step = 1.0):
    if stop == None:
        stop = start
        start = 0
    the_range = []
    start, stop, step = float(start), float(stop), float(step)
    while start < stop:
        the_range.append(start)
        start = round(start + step,3)
    print("(", end = '')
    for num in the_range:
        print(num, end = '')
        if num != the_range[-1]:
            print(", ", end = '')
    print(")")
    
print("*** New Range ***")
params = []
params = input("Enter Input : ").split(' ')
if len(params) == 1:
    range(params[0])
elif len(params) == 2:
    range(params[0], params[1])
elif len(params) == 3:
    range(params[0], params[1], params[2])
        

    