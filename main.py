from morse_code import morse_code_rules

word = input("What word would you like to convert to morse code?").lower()

#Method 1: #inputs into string
# converted_word = ''
#
# for char in word:
#     converted_word += morse_code_rules[char]
# print(converted_word)

#Method 2: #inputs into list
# converted_word = [''.join(morse_code_rules[char]) for char in word]
#
# print(converted_word)

#Method 3: #inputs into list then into a string
# converted_word = [''.join(morse_code_rules[char]) for char in word]
# endstring = ''
# for code in converted_word:
#     endstring += code + ' '
#
# print(endstring)

# Function
def convert_word(word):
    converted_word = [''.join(morse_code_rules[char]) for char in word]
    print(converted_word)

convert_word(word)