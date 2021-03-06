# Function to take only float input by Recursion

def get_float(msg = "Enter float: "):
    try:
        flt = float(input(msg))
    except ValueError:
        print("Invalid Input, enter a float...")
        flt = get_float(msg)
    return flt

# Lets try it out

price = get_float("Enter price: ")
flot = get_float()

print(price)
print(flot)



# Thank you !!!
