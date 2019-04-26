# --------------- Source -----------------
import random

#!/usr/bin/env python
__author__ = "Roei Burstein"

""" This program emulates a slot machine with random spins. Each
element of the slot machine has its own probability, and is displayed
through pulls, with each pull having a calculation for profit.
"""
# --------------- CONSTANTS -----------------

# Percentages for each outcome
BAR_RANGE = 45
CHERRIES_RANGE = 40
SPACE_RANGE = 5
SEVEN_RANGE = 10

MAX_BET_AMOUNT = 50
MIN_BET_AMOUNT = 0

# String names for items in slot machine
BAR = "BAR"
CHERRIES = "cherries"
SPACE = "space"
SEVEN = "7"

# Multiplier values
THREE_SEVENS = 100
THREE_BARS = 50
THREE_CHERRIES = 30
CHERRIES_IN_1_AND_2 = 15
CHERRY_IN_1 = 5

# Main method
def main():
   # Infinite loop (exists when user selects "0")
   while(True):
      bet_val = get_bet()
      if(bet_val == 0):
         print("Thank you for playing at Roei's Casino")
         exit(0)
      else:
         triple_string = pull()
         winnings = bet_val * get_pay_multiplier(triple_string)
         display(triple_string, winnings)

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

# --------------- Helper Methods -----------------

# Gets the bet from the user, checks for invalid input
def get_bet():
   while(True):
      num_bet = int(input("Bet amount (1 - 50) or 0 to quit: "))
      if MIN_BET_AMOUNT <= num_bet <= MAX_BET_AMOUNT: # Error checking
         return num_bet

# Creates TripleString object based on rand_string()
def pull():
   string_1 = rand_string()
   string_2 = rand_string()
   string_3 = rand_string()

   return TripleString(string_1, string_2, string_3)

# Selects a random string based on the probability percentage constants
def rand_string():
   rand_num = random.randrange(100) # Chooses random number between 0 and 99

   if 0 <= rand_num <= BAR_RANGE - 1: # Within BAR_RANGE probability
      return BAR

   # Within CHERRIES_RANGE probability
   elif BAR_RANGE <= rand_num <= BAR_RANGE + CHERRIES_RANGE - 1:
      return CHERRIES

   # Within SEVEN_RANGE probability
   elif BAR_RANGE + CHERRIES_RANGE <= rand_num \
      <= BAR_RANGE + CHERRIES_RANGE + SEVEN_RANGE - 1:
      return SEVEN
   # Within SPACE_RANGE probability (if it's not anything else)
   else:
      return SPACE

# Calculates the pay multiplier based on pull
def get_pay_multiplier(the_pull):
   string_1 = the_pull.get_string1()
   string_2 = the_pull.get_string2()
   string_3 = the_pull.get_string3()

   if string_1 == SEVEN and string_2 == SEVEN and string_3 == SEVEN:
      return THREE_SEVENS

   elif string_1 == BAR and string_2 == BAR and string_3 == BAR:
      return THREE_BARS

   # Checks if cherries is first pull, first and second, or all three
   elif string_1 == CHERRIES:
      if string_2 == CHERRIES:
         if string_3 == CHERRIES:
            return THREE_CHERRIES
         return CHERRIES_IN_1_AND_2
      return CHERRY_IN_1

   # If no multiplier applies
   else:
      return 0

# Displays the results
def display(the_pull, winnings):

   print("Spinning..... and your pull is.....\n")
   print(the_pull.to_string())

   if winnings == 0:
      print("Sorry, you lose!\n")

   else:
      print("Congratulations, you win $" + str(winnings) + "\n")

# --------------- Client -----------------
# Runs the main method defined above

main()

""" In the run below, pulls 2, 8, 25, 29, 34, 35, 43, 46, and 48 
resulted in BAR, BAR, BAR. Pulls 4, 32, and 45 resulted in
cherries, cherries, cherries.
"""

""" --------------- RUN -----------------
2, 8, 25, 29, 34, 35, 43, 46, 48
Bet amount (1 - 50) or 0 to quit: -5
Bet amount (1 - 50) or 0 to quit: 100
Bet amount (1 - 50) or 0 to quit: 1
Spinning..... and your pull is.....

BAR, 7, cherries
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 2
Spinning..... and your pull is.....

BAR, BAR, BAR
Congratulations, you win $100

Bet amount (1 - 50) or 0 to quit: 3
Spinning..... and your pull is.....

cherries, BAR, cherries
Congratulations, you win $15

Bet amount (1 - 50) or 0 to quit: 4
Spinning..... and your pull is.....

cherries, cherries, cherries
Congratulations, you win $120

Bet amount (1 - 50) or 0 to quit: 5
Spinning..... and your pull is.....

7, cherries, BAR
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 6
Spinning..... and your pull is.....

BAR, cherries, BAR
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 7
Spinning..... and your pull is.....

cherries, BAR, cherries
Congratulations, you win $35

Bet amount (1 - 50) or 0 to quit: 8
Spinning..... and your pull is.....

BAR, BAR, BAR
Congratulations, you win $400

Bet amount (1 - 50) or 0 to quit: 9
Spinning..... and your pull is.....

BAR, cherries, space
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 10
Spinning..... and your pull is.....

BAR, BAR, cherries
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 11
Spinning..... and your pull is.....

cherries, BAR, cherries
Congratulations, you win $55

Bet amount (1 - 50) or 0 to quit: 12
Spinning..... and your pull is.....

cherries, BAR, BAR
Congratulations, you win $60

Bet amount (1 - 50) or 0 to quit: 13
Spinning..... and your pull is.....

space, space, 7
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 14
Spinning..... and your pull is.....

7, 7, cherries
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 15
Spinning..... and your pull is.....

cherries, 7, BAR
Congratulations, you win $75

Bet amount (1 - 50) or 0 to quit: 16
Spinning..... and your pull is.....

cherries, 7, cherries
Congratulations, you win $80

Bet amount (1 - 50) or 0 to quit: 17
Spinning..... and your pull is.....

7, BAR, BAR
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 18
Spinning..... and your pull is.....

BAR, 7, BAR
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 19
Spinning..... and your pull is.....

7, cherries, BAR
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 20
Spinning..... and your pull is.....

7, 7, BAR
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 21
Spinning..... and your pull is.....

cherries, cherries, 7
Congratulations, you win $315

Bet amount (1 - 50) or 0 to quit: 22
Spinning..... and your pull is.....

cherries, 7, cherries
Congratulations, you win $110

Bet amount (1 - 50) or 0 to quit: 23
Spinning..... and your pull is.....

cherries, cherries, BAR
Congratulations, you win $345

Bet amount (1 - 50) or 0 to quit: 24
Spinning..... and your pull is.....

cherries, space, BAR
Congratulations, you win $120

Bet amount (1 - 50) or 0 to quit: 25
Spinning..... and your pull is.....

BAR, BAR, BAR
Congratulations, you win $1250

Bet amount (1 - 50) or 0 to quit: 26
Spinning..... and your pull is.....

cherries, BAR, cherries
Congratulations, you win $130

Bet amount (1 - 50) or 0 to quit: 27
Spinning..... and your pull is.....

cherries, cherries, 7
Congratulations, you win $405

Bet amount (1 - 50) or 0 to quit: 28
Spinning..... and your pull is.....

space, 7, cherries
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 29
Spinning..... and your pull is.....

BAR, BAR, BAR
Congratulations, you win $1450

Bet amount (1 - 50) or 0 to quit: 30
Spinning..... and your pull is.....

cherries, BAR, BAR
Congratulations, you win $150

Bet amount (1 - 50) or 0 to quit: 31
Spinning..... and your pull is.....

7, 7, BAR
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 32
Spinning..... and your pull is.....

cherries, cherries, cherries
Congratulations, you win $960

Bet amount (1 - 50) or 0 to quit: 33
Spinning..... and your pull is.....

BAR, cherries, 7
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 34
Spinning..... and your pull is.....

BAR, BAR, BAR
Congratulations, you win $1700

Bet amount (1 - 50) or 0 to quit: 35
Spinning..... and your pull is.....

BAR, BAR, BAR
Congratulations, you win $1750

Bet amount (1 - 50) or 0 to quit: 36
Spinning..... and your pull is.....

BAR, BAR, 7
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 37
Spinning..... and your pull is.....

BAR, cherries, cherries
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 38
Spinning..... and your pull is.....

cherries, cherries, BAR
Congratulations, you win $570

Bet amount (1 - 50) or 0 to quit: 39
Spinning..... and your pull is.....

BAR, BAR, space
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 40
Spinning..... and your pull is.....

cherries, space, cherries
Congratulations, you win $200

Bet amount (1 - 50) or 0 to quit: 41
Spinning..... and your pull is.....

BAR, BAR, cherries
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 42
Spinning..... and your pull is.....

BAR, cherries, cherries
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 43
Spinning..... and your pull is.....

BAR, BAR, BAR
Congratulations, you win $2150

Bet amount (1 - 50) or 0 to quit: 44
Spinning..... and your pull is.....

space, BAR, BAR
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 45
Spinning..... and your pull is.....

cherries, cherries, cherries
Congratulations, you win $1350

Bet amount (1 - 50) or 0 to quit: 46
Spinning..... and your pull is.....

BAR, BAR, BAR
Congratulations, you win $2300

Bet amount (1 - 50) or 0 to quit: 47
Spinning..... and your pull is.....

cherries, 7, 7
Congratulations, you win $235

Bet amount (1 - 50) or 0 to quit: 48
Spinning..... and your pull is.....

BAR, BAR, BAR
Congratulations, you win $2400

Bet amount (1 - 50) or 0 to quit: 49
Spinning..... and your pull is.....

BAR, cherries, BAR
Sorry, you lose!

Bet amount (1 - 50) or 0 to quit: 50
Spinning..... and your pull is.....

cherries, BAR, cherries
Congratulations, you win $250

Bet amount (1 - 50) or 0 to quit: 0
Thank you for playing at Roei's Casino
"""