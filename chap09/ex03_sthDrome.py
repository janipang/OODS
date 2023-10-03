def dromeCheck(array):
    if(isRepdrome(array)):
        return "Repdrome"
    elif(isMetadrome(array)):
        return "Metadrome"
    elif(isPlaindrome(array)):
       return "Plaindrome"
    elif(isKatadrome(array)):
        return "Katadrome"
    elif(isNialpdrome(array)):
        return "Nialpdrome"
    else:
        return "Nondrome"


def isRepdrome(array):
    if len(array) < 2:
        return 1
    return (array[0] == array[1]) and isRepdrome(array[1:])

def isMetadrome(array):
    if len(array) < 2:
        return 1
    return (array[0] < array[1]) and isMetadrome(array[1:])

def isPlaindrome(array):
    if len(array) < 2:
        return 1
    return (array[0] <= array[1]) and isPlaindrome(array[1:])

def isKatadrome(array):
    if len(array) < 2:
        return 1
    return (array[0] > array[1]) and isKatadrome(array[1:])

def isNialpdrome(array):
    if len(array) < 2:
        return 1
    return (array[0] >= array[1]) and isNialpdrome(array[1:])

nums = [int(i) for i in input("Enter Input : ")]
print(dromeCheck(nums))