# Begin with numbers
print((3 + 1.5 + 4) ** (2))

# Strings
s = 'hello'
# Indexing begins with 0
print(s[1])
# Reverse the string. 3rd parameter is step.
print(s[::-1])

# Lists
list4 = [5,3,4,6,1]
# Method 1
print(sorted(list4))
# Method 2
list4.sort()
print(list4)

list3 = [1,2,[3,4,'hello']]
list3[-1][-1] = 'goodbye'
print(list3)

# Dictionaries
d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])