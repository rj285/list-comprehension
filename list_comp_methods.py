# Squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Squares of even numbers from 0 to 9
squares_even = [x**2 for x in range(10) if x % 2 == 0]
print(squares_even)  # Output: [0, 4, 16, 36, 64]

# Lengths of the given names
names = ["jazil", "abhi", "fhs", "richin", "sanjay", "sooraj"]
lengths = [len(x) for x in names]
print(lengths)  # Output: [5, 4, 3, 6, 6, 6]

# Vowels in the input word
text = input("Enter the word to check vowels: ")
vowels = [x for x in text if x in "aeiouAEIOU"]
print(vowels)  # Output depends on the input

# Pairs from two lists using zip
list1 = ["yasin", "abhi", "sooraj", "fhs", "richin"]
list2 = ["usa", "calicut", "japan", "malapuram", "university"]
result = [(x, y) for x, y in zip(list1, list2)]
print(result)  # Output: [('yasin', 'usa'), ('abhi', 'calicut'), ...]

# Convert names to uppercase
names = ['yasin', 'sooraj', 'fhs', 'abhi', 'sanjay']
upper_names = [item.upper() for item in names]
print(upper_names)  # Output: ['YASIN', 'SOORAJ', 'FHS', 'ABHI', 'SANJAY']
