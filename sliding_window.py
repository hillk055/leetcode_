"""Create a function that counts the number of arrays of size k that sum to a value of larger than 10 in o(n) time"""

nums = [3, 5, 2, 7, 4, 1]
k = 3
count = 0
sum = 0
left = 0

for right in range(len(nums)):

    sum += nums[right]
    if right - left + 1 == k:
        if sum > 10:
            count += 1
        sum -= nums[left]
        left += 1

print(count)

"""Create a function that find the smallest array that is larger than or equal to the target value"""

nums = [2, 3, 1, 2, 4, 3]
target = 7

left = 0
sum = 0
shortest_array = 100000

for right in range(len(nums)):
    sum += nums[right]
    if sum >= target: #Keep moving right until the sum is either equal to or larger than the target
        while sum >= target:
            shortest_array = min(shortest_array, right - left + 1) # Store the shortest array
            sum -= nums[left] # Remove the value of the first value of the window and increment left by 1, we know have one less value in the window. Rerun the condition in the while
                              # loop to see if the sum is still above the target. if it is we can update the shortest array again
            left += 1


print(shortest_array)



