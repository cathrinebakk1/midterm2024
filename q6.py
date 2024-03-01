original_string = "Hello, World!"
# Attempting to change the first character to 'J'
try:
  original_string[0] = 'J'
except TypeError as e:
  print(f"Error: {e}")

# Correct way to modify a string
modified_string = 'J' + original_string[1:]
print(modified_string) # This will print "Jello, World!"

# Lists can be changed.
my_list = [1, 2, 3]
my_list[0] = 10  # Changing the first element to 10
print(my_list)  # This will print [10, 2, 3]
