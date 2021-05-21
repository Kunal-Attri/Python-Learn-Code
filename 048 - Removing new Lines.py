# Removing new lines from a string

data = ['alpha\n', 'beta\n', 'gamma\n']

print("Raw data: ", data)

# Method 1: using strip predefined method
m1 = [s.strip() for s in data]
print("Method 1: ", m1)

# Method 2: this time with map
def strip(s):
    return s.strip()
m2 = list(map(strip, data))    # map returns map object, fo converting
print("Method 1: ", m2)

# Method 3: now with a lambda function
m3 = list(map(lambda s: s.strip(), data)) 
print("Method 3: ", m3)

# Thank You !!!
