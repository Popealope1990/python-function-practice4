# Practice function 1
print("Practice Function 1")

def max_num(a, b, c):
    return max([a, b, c])

print(max_num(1,20,4))
print(max_num(15,25,38))

# Practice function 2
print("Practice Function 2")

def mult_list(nums):
    res = nums[0]
    for n in nums[1:]:
        res = res * n

    return res

print(mult_list([10, 10]))
print(mult_list([11, 12, 13]))

# Practice functin 3
print("Practice Function 3")

def rev_string(string):
    return string[::-1]

print(rev_string("Hello"))
print(rev_string("racecar"))


# Practice function 4
print("Practice Function 4")

def num_within(a,b,c):
    return a in range(b,c)

print(num_within(3,1,4))
print(num_within(5,3,7))
print(num_within(1,2,5))