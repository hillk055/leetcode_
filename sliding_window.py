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

"""Find the longest substring containing at most k unique characters"""

s = "eceba"
k = 2
left = 0
longest_sub_string = 0
chars = {}

for right in range(len(s)):    # Start adding one to the right window

    if s[right] in chars:
        chars[s[right]] += 1
    else:
        chars[s[right]] = 1    # Store the number of counts of characters, add a key if a new character appears

    if len(chars) > k:    # If we have more than k characters
        while len(chars) > k:    # While more than k characters, delete the first character on the left and increment left by 1, keep going until only k unique characters remain
            chars[s[left]] -= 1
            if chars[s[left]] == 0:
                del chars[s[left]]    # Because we are using length if the count of a character reaches 0 we need to remove it otherwise the condition will always be satisfied.
            left += 1

    longest_sub_string = max(longest_sub_string, right - left + 1)    # Add after the condition so that we update the longest before we have more than k unique characters

print(longest_sub_string)

"""Find the longest substring containing k unique characters"""

s = "araaci"
k = 2
left = 0
longest_string = 0
chars = {}

for right in range(len(s)):
    if s[right] in chars:
        chars[s[right]] += 1
    else:
        chars[s[right]] = 1

    if len(chars) > k:
        chars[s[left]] -= 1
        if chars[s[left]] == 0:
            del chars[s[left]]
        left += 1

    if len(chars) == 2:
        longest_string = max(longest_string, right - left + 1)


print(longest_string)





