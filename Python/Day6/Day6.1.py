import sys

nums = []
f = open('Day6List.txt', 'rU')
f = f.read()
f = f.split()
for val in f:
    nums.append(int(val))

track = []
track.append(str(nums))
n = nums.index(max(nums)) + 1
count = max(nums)
nums[n - 1] = 0

while len(track) < 5000:
    if count > 0:
        if n == len(nums) - 1:
            nums[n] = nums[n] + 1
            count = count - 1
            n = 0
        else:
            nums[n] = nums[n] + 1
            count = count - 1
            n = n + 1
    elif count == 0:
        for val in track:
            if val == str(nums):
                print(len(track))
                sys.exit()
        else:
            track.append(str(nums))
            n = nums.index(max(nums))
            count = max(nums)
            nums[n] = 0
            if n == len(nums) - 1:
                n = 0
            else:
                n = n + 1