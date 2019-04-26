# --------------- Source -----------------
#!/usr/bin/env python
__author__ = "Roei Burstein"

""" This program simulates a frozen yogurt cash register and all of
its operations. The cash register allows the user to make purchases and gain
stamps, or use 9 stamps to get one free frozen yogurt. The cash register
checks for invalid inputs for the menu options and the quantities.
"""

num_stamps = 0 # Number of stamps the user has
STAMPS_FOR_FREE_YOGURT = 9 # Number of stamps for free yogurt
INDENT = "   " # Indentation of 3 spaces

# Initialize boolean constants as false to enter while loops
starts_with_s = False
starts_with_p = False
used_stamps = False

while(True): # Primary loop
   while not starts_with_s and not starts_with_p: # Checks if invalid input
      print("Menu Options:")
      print(INDENT + "P (Purchase)")
      print(INDENT + "S (Shut Down)\n")
      menu_choice = input("What would you like to choose? ")

      starts_with_s = (menu_choice.startswith('s') or # True if starts with s
      menu_choice.startswith('S'))

      starts_with_p = (menu_choice.startswith('p') or # True if starts with p
      menu_choice.startswith('P'))

      if (not starts_with_s and not starts_with_p): # Checks if invalid input
         print("\n*** Choose either 'P' or 'S' please :) ***\n")
      elif(starts_with_s): # If starts with s, shut down register
         print("Thank you, goodbye")
         exit(0)
   if(num_stamps >= STAMPS_FOR_FREE_YOGURT): # True if free yogurt possible
      user_input = input("You qualify for one free yogurt in exchange "
      "for " + str(STAMPS_FOR_FREE_YOGURT)
      + " stamps.\nWould you like to use them? ('Y' or 'N') ")

      # Checks if user selected 'yes' to getting free yogurt
      if(user_input.startswith('y') or user_input.startswith('Y')):
         num_stamps -= STAMPS_FOR_FREE_YOGURT
         print("\nYou've just used " + str(STAMPS_FOR_FREE_YOGURT) +
         " stamps for one yogurt. You have " + str(num_stamps) +
         " stamps remaining.\n")
         used_stamps = True

   # Checks if user either said no for free yogurt or doesn't qualify for it
   if((num_stamps < STAMPS_FOR_FREE_YOGURT or user_input.startswith('n')
      or user_input.startswith('N')) and not used_stamps):

      num_yogurts = int(input("How many yogurts would you like to purchase? "))
      if(num_yogurts <= 0): # Bounds check that only allows positive yogurt num
         print("\n*** Invalid number of yogurts ***\n")

      else:
         num_stamps += num_yogurts
         print("\nYou Just earned " + str(num_yogurts) +
         " stamps and have a total of " + str(num_stamps) + " to use\n")

   # Resets booleans to false for new run
   starts_with_s = False
   starts_with_p = False
   used_stamps = False

""" --------------- RUNS -----------------

---- Run 1 ----

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? Purchase
How many yogurts would you like to purchase? -3

*** Invalid number of yogurts ***

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? 6

*** Choose either 'P' or 'S' please :) ***

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? Purchase
How many yogurts would you like to purchase? 9

You Just earned 9 stamps and have a total of 9 to use

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? ppppppp
You qualify for one free yogurt in exchange for 9 stamps.
Would you like to use them? ('Y' or 'N') N
How many yogurts would you like to purchase? 12

You Just earned 12 stamps and have a total of 21 to use

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? P
You qualify for one free yogurt in exchange for 9 stamps.
Would you like to use them? ('Y' or 'N') Y

You've just used 9 stamps for one yogurt. You have 12 stamps remaining.

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? abcd

*** Choose either 'P' or 'S' please :) ***

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? P
You qualify for one free yogurt in exchange for 9 stamps.
Would you like to use them? ('Y' or 'N') N
How many yogurts would you like to purchase? -4

*** Invalid number of yogurts ***

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? P
You qualify for one free yogurt in exchange for 9 stamps.
Would you like to use them? ('Y' or 'N') Y

You've just used 9 stamps for one yogurt. You have 3 stamps remaining.

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? shut down
Thank you, goodbye

Process finished with exit code 0
________________________________________________________________

---- Run 2 ----

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? penelope
How many yogurts would you like to purchase? 0

*** Invalid number of yogurts ***

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? 'purchase

*** Choose either 'P' or 'S' please :) ***

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? p
How many yogurts would you like to purchase? 8

You Just earned 8 stamps and have a total of 8 to use

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? Purchase please my friend!
How many yogurts would you like to purchase? 2

You Just earned 2 stamps and have a total of 10 to use

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? a

*** Choose either 'P' or 'S' please :) ***

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? b

*** Choose either 'P' or 'S' please :) ***

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? c

*** Choose either 'P' or 'S' please :) ***

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? p
You qualify for one free yogurt in exchange for 9 stamps.
Would you like to use them? ('Y' or 'N') N
How many yogurts would you like to purchase? 1

You Just earned 1 stamps and have a total of 11 to use

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? P
You qualify for one free yogurt in exchange for 9 stamps.
Would you like to use them? ('Y' or 'N') asdf
Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? P
You qualify for one free yogurt in exchange for 9 stamps.
Would you like to use them? ('Y' or 'N') yes

You've just used 9 stamps for one yogurt. You have 2 stamps remaining.

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? p u r c h a s e
How many yogurts would you like to purchase? 3

You Just earned 3 stamps and have a total of 5 to use

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? P
How many yogurts would you like to purchase? -11

*** Invalid number of yogurts ***

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? 4

*** Choose either 'P' or 'S' please :) ***

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? pur
How many yogurts would you like to purchase? 9

You Just earned 9 stamps and have a total of 14 to use

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? o

*** Choose either 'P' or 'S' please :) ***

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? p
You qualify for one free yogurt in exchange for 9 stamps.
Would you like to use them? ('Y' or 'N') Y

You've just used 9 stamps for one yogurt. You have 5 stamps remaining.

Menu Options:
   P (Purchase)
   S (Shut Down)

What would you like to choose? s
Thank you, goodbye

Process finished with exit code 0
-------------------------------------- """