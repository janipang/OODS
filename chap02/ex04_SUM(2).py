nums = list(map(int, input("Enter Your List : ").split(' ')))

ans = []
real_ans = []
if len(nums) < 3:
    print("Array Input Length Must More Than 2")
    exit()
    
for i in range(len(nums) - 2):
    for j in range(i + 1, len(nums) - 1):
        for k in range(j + 1, len(nums) - 0):
            if nums[i] + nums[j] + nums[k] == 5:
                ans.append([nums[i], nums[j], nums[k]])

for sub_ans in ans:
    to_append = 1
    for each_real_ans in real_ans:
        if min(sub_ans) == min(each_real_ans) and max(sub_ans) == max(each_real_ans):
            to_append = 0
    if to_append:
        real_ans.append(sub_ans)

for sub_real in real_ans:
    sub_real.sort()
            
print(real_ans)