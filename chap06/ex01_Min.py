nums = list(map(int, input("Enter Input : ").split(" ")))
lowest = nums[0]

def find_min(lowest):
    if len(nums) > 0:
        if lowest > nums[0]:
            lowest = nums.pop(0)
        else:
            nums.pop(0)
        find_min(lowest)
    else:
        print(f"Min : {lowest}")
        
find_min(lowest)