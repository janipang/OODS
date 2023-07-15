print(" *** String count ***")

text = str(input("Enter message : "))

up_count = 0
low_count = 0

char_list = [0]*128

for alpha in text:
    if alpha.isupper():
        char_list[ord(alpha)] += 1
        up_count += 1
    if alpha.islower():
        char_list[ord(alpha)] += 1
        low_count += 1

print("No. of Upper case characters : " + str(up_count))
print("Unique Upper case characters : ", end = '')
for num in range(128):
    if char_list[num] > 0 and chr(num).isupper() :
        print(chr(num), end = '  ')
print("\nNo. of Lower case Characters : " + str(low_count))
print("Unique Lower case characters : ", end = '')
for num in range(128):
    if char_list[num] > 0 and chr(num).islower() :
        print(chr(num), end = '  ')