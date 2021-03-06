# Understanding Try - Except - Else block

# Sometimes in python, a scenario arises where your program
# might give an error and get crash. eg converting a non-
# integer based string into a integer gives ValueError

a = "10"

try:
    # Code which might give an error
    b = int(a)
    print(b)
except ValueError:    # Error which might be arised
    # Code which should be executed if error arises
    print("a does not contain integer")
# Optionally else block is also there
else:
    # Code to be executed if no error arises
    print("Successfully converted into integer")



# Thank You !!!
