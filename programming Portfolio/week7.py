#1.Write and test a function that takes a string as a parameter and returns a sorted list
#of all the unique letters used in the string. So, if the string is cheese, the list
#returned should be ['c', 'e', 'h', 's'].

def sorted_letters(input_string):
    input_string = input_string.lower()
    unique_letters = sorted(set(char for char in input_string if char.isalpha()))

    return unique_letters

# Testing the function 
result =sorted_letters("cheese")
print(result)
print()



#2.Write and test three functions that each take two words (strings) as parameters and
#return sorted lists (as defined above) representing respectively:
    #Letters that appear in at least one of the two words.
    #Letters that appear in both words.
    #Letters that appear in either word, but not in both.

def letters_in_either(word1, word2):
    common = set(word1) & set(word2)
    return sorted(list(common))

def letters_either_not_both(word1, word2):
    unique = set(word1) ^ set(word2)
    return sorted(list(unique))

def letters_in_both(word1, word2):
    shared = set(word1) & set(word2)
    unique_word1 = set(word1) - shared
    unique_word2 = set(word2) - shared
    return sorted(list(shared)), sorted(list(unique_word1)), sorted(list(unique_word2))

#Test the functions with words "hello" and "world"
result_either = letters_in_either("hello","world")
result_both = letters_in_both("hello","world")
result_either_not_both = letters_either_not_both("hello","world")

print("Letters in either word:", result_either)
print("Letters in both words:", result_both)
print("Letters in either, but not both:", result_either_not_both)
print()



#3.Write a program that manages a list of countries and their capital cities. It should
#prompt the user to enter the name of a country. If the program already "knows"
#the name of the capital city, it should display it. Otherwise it should ask the user to
#enter it. This should carry on until the user terminates the program (how this
#happens is up to you).



country_capitals = {}


while True:
    
    country_name = input("Enter the name of a country (or type 'exit' to end): ")
    if country_name.lower() == 'exit':
        break

    
    if country_name in country_capitals:
        print(f"The capital of {country_name} is {country_capitals[country_name]}.")
    else:
        capital_city = input(f"The capital of {country_name} is not known. Enter the capital city: ")
        country_capitals[country_name] = capital_city
        print(f"Thank you! The capital of {country_name} ({capital_city}) has been added to the database.")


print("\nCountries and their capitals:")

for country, capital in country_capitals.items():
    print(f"{country}: {capital}")
    print()



#4.Write a program that processes a string representing a message and reports the six
#most common letters, along with the number of times they appear. Case should
#not matter, so "E" and "e" are considered the same.
    
from collections import Counter

def frequency_analysis(message):
    message = message.lower()

    char_counts = Counter(char for char in message if char.isalpha())
    most_common = char_counts.most_common(6)
    print("Six most common letters and their counts:")
    for char, count in most_common:
        print(f"{char}: {count}")

# Example usage:
encrypted_message = "Hello WORLDE.Thns bdyubhjd eb wsHBAHj f"
frequency_analysis(encrypted_message)