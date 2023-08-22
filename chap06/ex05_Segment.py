# def striping(part):
#     if len(part) == 0:
#         parts = []
#     else:
#         temp = part.pop(0).strip().strip("\'")
#         parts = striping(part)
#         parts.append(temp)
#     return parts
        
# data = input("Enter list[str]: ")
# part = list(map(str, data.split(',')))
# print(part)
# parts = striping(part)
# parts.reverse()
# word = parts.pop(0)
# print(parts)
# ########################################################33

inp = input('Enter list[str]: ').split("'")[1::2]
word, parts = inp[0], inp[1:]

def segment(text, word_list):
    if not text:
        return True
    
    if not word_list:
        return False
    
    word = word_list[0]
    if word and word in text:
        remaining_text = text.replace(word, "", 1)
        if segment(remaining_text, word_list) or segment(text, word_list[1:]):
            return True
        
    return segment(text, word_list[1:])

print(f"text: str = '{word}'")
print(f"lang: list[str] = {parts}")
print(f"segment(text, lang) -> {segment(word, parts)}")
    
