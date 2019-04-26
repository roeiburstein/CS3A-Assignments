# --------------- Source -----------------
#!/usr/bin/env python
__author__ = "Roei Burstein"

""" This program manipulates every instance of a certain character within it.
The user enters a key character and a string, and the program does 
three actions: Replace all key character occurrences within the string with
and asterisk, remove all key character occurrences within the string, and
count the number of instances of the key character within the string.
"""
# --------------- Constants -----------------
ASTERISK = '*'
CHAR_LENGTH = 1
STRING_MIN_LENGTH = 6
STRING_MAX_LENGTH = 500
INDENT = "   "


# --------- Function Definitions ------------
def get_key_character():
   """Requests single character from user.
      :return: Valid character given by user.
   """
   user_input = ""
   while len(user_input) != CHAR_LENGTH: # Loops until user enters single char
      user_input = input("Please enter a single character: ")
   return user_input # Returns the user input

def get_string():
   """Requests string from user.
      :return: Valid string given by user.
   """
   user_input = ""
   # Loops until user input is within the sentence range
   while len(user_input) not in range(STRING_MIN_LENGTH, STRING_MAX_LENGTH):
      user_input = input("Please enter a string (more than six characters): ")
   return user_input # Returns the user input

def mask_character(the_string, key_character):
   """Takes one string and one character.
      Replaces all instances of character with '*'.
      :return: New string with characters changed.
   """
   temp_string = ""
   for c in the_string: # Loops through every character in the string
      if c == key_character: # Checks if character equals the key character
         temp_string += ASTERISK
      else: # Checks if character does not equal key character
         temp_string += c
   return temp_string # Returns the updated string

def remove_character(the_string, key_character):
   """Takes one string and one character.
      Removes all instances of character from string.
      :return: New string with characters removed.
   """
   temp_string = ""
   for c in the_string: # Loops through every character in the string
      if c != key_character: # Checks if character does not equal key
         temp_string += c

   return temp_string # Returns the updated string

def count_key(the_string, key_character):
   """Takes one string and one character.
      Counts all instances of character from string.
      :return: Number of instances of character in string.
   """
   char_count = 0
   for c in the_string: # Loops through every character in the string
      if c == key_character: # Checks if character equals the key character
         char_count += 1
   return char_count # Returns number of occurrences of key character

# ------------ Main Program --------------

key_char = get_key_character()
my_string = get_string()
masked_string = mask_character(my_string, key_char)
removed_string = remove_character(my_string, key_char)
num_occurrences = count_key(my_string, key_char)

print("\nStarting with key character, '" + key_char + "', masked: ")
print(INDENT + "'" + masked_string + "'")
print("\n\nStarting with '" + key_char + "' removed: ")
print(INDENT + "'" + removed_string + "'")
print("\n\n# of occurrences of key character '" + key_char + "': " +
str(num_occurrences))

""" --------------- RUNS -----------------

---- Run 1 ----


Please enter a single character: 1234
Please enter a single character: 
Please enter a single character: a
Please enter a string (more than six characters): abcde
Please enter a string (more than six characters): abra cadabra

Starting with key character, 'a', masked: 
   '*br* c*d*br*'


Starting with 'a' removed: 
   'br cdbr'


# of occurrences of key character 'a': 5

Process finished with exit code 0



---- Run 2 ----


Please enter a single character: 1
Please enter a string (more than six characters): 10000111 11101010 10110010

Starting with key character, '1', masked: 
   '*0000*** ***0*0*0 *0**00*0'


Starting with '1' removed: 
   '0000 000 0000'


# of occurrences of key character '1': 13

Process finished with exit code 0



---- Run 3 ----


Please enter a single character: o
Please enter a string (more than six characters): O
Please enter a string (more than six characters): OooOOoOoooOoooOOOOOo

Starting with key character, 'o', masked: 
   'O**OO*O***O***OOOOO*'


Starting with 'o' removed: 
   'OOOOOOOOOO'


# of occurrences of key character 'o': 10

Process finished with exit code 0



---- Run 4 ----



Please enter a single character: ~
Please enter a string (more than six characters): !~&#^@*&^$!*&~@*$&~^

Starting with key character, '~', masked: 
   '!*&#^@*&^$!*&*@*$&*^'


Starting with '~' removed: 
   '!&#^@*&^$!*&@*$&^'


# of occurrences of key character '~': 3

Process finished with exit code 0

"""
