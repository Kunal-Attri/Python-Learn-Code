# Importing user modules

# To import module, lets first create one
# Let's import greet method from utils.py

# Method 1
import utils
print("Method 1")
utils.greet("Rahul")
utils.greet("Kunal")
utils.greet("Preeti")


# Method 2: direct calling
from utils import greet
print("Method 2")
greet("Rahul")
greet("Kunal")
greet("Preeti")



# Thank You !!!
