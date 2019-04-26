# --------------- Source -----------------

#!/usr/bin/env python
__author__ = "Roei Burstein"

""" This program creates an object called TripleString which contains three
string parameters (as the name suggests). This object is in its own class and
has accessor and mutator functionality.
"""

# Main method
def main():
   ts1 = TripleString("hello", "hi", "hey")
   ts2 = TripleString("alpha", "beta", "gamma")
   ts3 = TripleString("Alabama", "Alaska") #string3 is default
   ts4 = TripleString("A")
   print("Display Original Objects:\n1. " + ts1.to_string() + "\n2. "
         + ts2.to_string() + "\n3. " + ts3.to_string()
         + "\n4. " + ts4.to_string())

   ts1.set_string1("salutations")
   ts2.set_string2("bravo")
   ts2.set_string3("charlie")
   ts3.set_string3("Arizona")
   ts4.set_string1("Z")

   print("\nDisplay Updated Objects:\n1. " + ts1.to_string() + "\n2. "
         + ts2.to_string() + "\n3. " + ts3.to_string()
         + "\n4. " + ts4.to_string())

   print("\nAttempting to insert 'Y' into ts4 string 2: ")
   if(ts4.set_string2("Y")): #True if input string is valid
      print("The mutation was successful")
   else:
      print("The mutation was not successful")

   print("\nAttempting to insert '' into ts4 string 3: ")
   if(ts4.set_string3("")): #True if input string is valid
      print("The mutation was successful")
   else:
      print("The mutation was not successful")

   print("\nAccessing ts1 string 1: " + ts1.get_string1())
   print("Accessing ts2 string 3: " + ts2.get_string3())

class TripleString:

   # --------------- Constants -----------------
   MIN_LENGTH = 1
   MAX_LENGTH = 50
   DEFAULT_STRING = "(undefined)"

   # --------------- Constructor -----------------
   def __init__(self, string1 = DEFAULT_STRING,
                string2 = DEFAULT_STRING, string3 = DEFAULT_STRING):
      if not self.set_string1(string1):
         self.string1 = self.DEFAULT_STRING
      if not self.set_string2(string2):
         self.string2 = self.DEFAULT_STRING
      if not self.set_string3(string3):
         self.string3 = self.DEFAULT_STRING

   # --------------- Mutators -----------------

   # Sets string1 for the TripleString object
   def set_string1(self, string):
      if self.valid_string(string): # True if the string is valid
         self.string1 = string
         return True
      else:
         return False

   # Sets string2 for the TripleString object
   def set_string2(self, string):
      if self.valid_string(string): # True if the string is valid
         self.string2 = string
         return True
      else:
         return False

   # Sets string3 for the TripleString object
   def set_string3(self, string):
      if self.valid_string(string): # True if the string is valid
         self.string3 = string
         return True
      else:
         return False

   # --------------- Accessors -----------------

   # Sets string1 for the TripleString object
   def get_string1(self):
      return self.string1

   # Sets string2 for the TripleString object
   def get_string2(self):
      return self.string2

   # Sets string3 for the TripleString object
   def get_string3(self):
      return self.string3

   # Prints out all the strings in the TripleString object
   def to_string(self):
      return self.string1 + ", " + self.string2 + ", " + self.string3


   # --------------- Helper Methods -----------------

   # Checks if the string is valid (within the length requirements)
   def valid_string(self, the_str):
      return len(the_str) >= self.MIN_LENGTH and len(the_str) <= self.MAX_LENGTH

# --------------- Client -----------------
# Runs the main method defined above
main()

""" --------------- RUN -----------------

Display Original Objects:
1. hello, hi, hey
2. alpha, beta, gamma
3. Alabama, Alaska, (undefined)
4. A, (undefined), (undefined)

Display Updated Objects:
1. salutations, hi, hey
2. alpha, bravo, charlie
3. Alabama, Alaska, Arizona
4. Z, (undefined), (undefined)

Attempting to insert 'Y' into ts4 string 2: 
The mutation was successful

Attempting to insert '' into ts4 string 3: 
The mutation was not successful

Accessing ts1 string 1: salutations
Accessing ts2 string 3: charlie

"""
