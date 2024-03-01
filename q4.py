# Define the function as provided
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

# Test each number to see if it is a palindrome
numbers = [
    "2704702208931031198668911301398022074072",
    "0974101607733149676776769413377061014790",
    "7798338247658278460338648728567428338977",
    "4257304920394478392772938744930294037524"
]

# Check each number using the palindrome function and list non-palindromes
non_palindromes = [num for num in numbers if not palindrome(num)]

print(non_palindromes)
