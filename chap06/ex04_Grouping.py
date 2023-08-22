text, pt = input("input number : ").split(",")
pt = int(pt) - 1
st, en, cnt = -1, -1, 1

def recursion():
    global pt, st, en, cnt
    if st == -1:
        if pt > 0 and text[pt-1] == text[pt]:
            pt -= 1
            recursion()
        else:
            st = pt
    if en == -1 and st != -1:
        if st < len(text) - 1 and text[st+1] == text[st]:
            cnt += 1
            st +=1
            recursion()
        else:
            en = st
            print(f"Character : {text[st]}")
            print(f"Count : {cnt}")
    
if text == "":
    print("Output : List is entry")
elif pt > len(text):
    print("Output : Pin number out of range")
elif pt < 1:
    print("Output : Pin number less than 1")
else:
    recursion()
