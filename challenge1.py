"""

#Challenge 1
int1 = [int(x) for x in input("Enter a seies of numbers seperated by spaces: ").split()]
sum = 0
for num in int1:
    sum += num

print("The sum of the numbers is: ",sum)

#Challenge 2
tuple1 = ("Blossoms of the Savanna", "Kigogo", "Chozi la heri")
for tuple in tuple1:
    print(tuple)

#Challenge 3
# Initialize an empty dictionary
person_info = {}

person_info['name'] = input("Enter your name: ")
person_info['age'] = int(input("Enter your age: "))
person_info['favorite_color'] = input("Enter your favorite color: ")

# Print the dictionary to the console
print("Person information: ", person_info)

#Challenge 4
set1 = {int(x) for x in input("Enter a set of 4 numbers: ").split(" ")}
set2 = {int (y) for y in input("Enter another set of 4 numbers: ").split(" ")}
common = (set1 & set2)
print("Common elements are : ", common)
"""

#Challenge 5
#words = [str (x) for x in input("Enter 3 words:").split(' ')]
#if len(words) % 2 != 0:
#    print(words)

# Initialize an empty list
word_list = []

# Ask the user how many words they want to add
num_words = str(input("Enter the number of words you want to add: "))

# Use a for loop to collect words from the user
for i in range(num_words):
    word = input(f"Enter word {i+1}: ")
    word_list.append(word)

# Use list comprehension to create a new list that contains only the words that have an odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2!= 0]

# Print the resulting list
print("Words with an odd number of characters: ", odd_length_words)