inpt = input("Enter Input : ")
text = []
text[:] = inpt

def palindrome(string):
    if len(string) > 1:
        if string[0] == string[-1]:
            string.pop(0)
            string.pop()
            palindrome(string)
        else:
            print(f"'{inpt}' is not palindrome")
    else:
        print(f"'{inpt}' is palindrome")
        
palindrome(text)