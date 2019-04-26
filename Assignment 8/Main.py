# --------------- Source -----------------

#!/usr/bin/env python
__author__ = "Roei Burstein"

""" This program simulates a dating app with different applicants looking
for different things. It takes into account a person's gender preferences, 
financial interests, romance, and distance when finding a potential partner. 
It returns the compatibility as a number between 0 and 1 between two people.
"""

# Main method
def main():

   # Creating four applicants
   applicant1 = DateProfile("M", "F", 5, 3, 1, "Robert Dawson")
   applicant2 = DateProfile("F", "F", 4, 8, 9, "Rolanda Perry")
   applicant3 = DateProfile("F", "M", 10, 0, 1, "Cheryl Landon")
   applicant4 = DateProfile("F", "F", 7, 4, 2, "Denise Deduncan")

   print("----PART 1 - NO LISTS:----\n")
   print(str(applicant1) + str(applicant2) + str(applicant3) + str(applicant4))

   display_two_profiles(applicant1, applicant1)
   display_two_profiles(applicant1, applicant2)
   display_two_profiles(applicant1, applicant3)
   display_two_profiles(applicant1, applicant4)

   print("\n")
   display_two_profiles(applicant2, applicant1)
   display_two_profiles(applicant2, applicant2)
   display_two_profiles(applicant2, applicant3)
   display_two_profiles(applicant2, applicant4)

   print("\n")
   display_two_profiles(applicant3, applicant1)
   display_two_profiles(applicant3, applicant2)
   display_two_profiles(applicant3, applicant3)
   display_two_profiles(applicant3, applicant4)

   print("\n")
   display_two_profiles(applicant4, applicant1)
   display_two_profiles(applicant4, applicant2)
   display_two_profiles(applicant4, applicant3)
   display_two_profiles(applicant4, applicant4)

   print("\n----PART 2 - LIST OF OBJECTS:----\n")
   list = [applicant1, applicant2, applicant3, applicant4]
   for applicant in list:
      print(str(applicant))

   for i in range(4):
      for j in range(4):
         display_two_profiles(list[i], list[j])
      print("\n")

   print("\n----PART 3 - USING THE MUTATORS:----\n")
   print("\nSetting the name of applicant1 to Roger Smith:")
   if(applicant1.set_name("Roger Smith")):
      print("Accepted input")
   else:
      print("Invalid input")

   print("\nSetting the finance of applicant2 to -5:")
   if(applicant2.set_finance(-5)):
      print("Accepted input")
   else:
      print("Invalid input")

   print("\nSetting the gender of applicant3 to m:")
   if(applicant3.set_gender("m")):
      print("Accepted input")
   else:
      print("Invalid input")

   print("\nSetting the gender of applicant4 to e:")
   if(applicant4.set_gender("p")):
      print("Accepted input")
   else:
      print("Invalid input")

   print("\nRe-printing mutated applicants: ")
   print(str(applicant1) + str(applicant2) + str(applicant3) + str(applicant4))

# Displays the fits between two profiles
def display_two_profiles(profile1, profile2):
   print("Fit between " + profile1.get_name() + " and " + profile2.get_name()
   + ":\t" + str(profile1.fit_value(profile2)))

class DateProfile:
   # --------------- CONSTANTS -----------------

   MIN_INT = 1
   MAX_INT = 10
   MIN_NAME_LEN = 1
   MAX_NAME_LEN = 50
   NUM_FIT_PARAMS = 3

   DEFAULT_GEND = "M"
   DEFAULT_SEARCH_GEND = "F"
   DEFAULT_NAME = "Nameless"
   DEFAULT_INT = 1

   # --------------- Constructor -----------------

   def __init__(self, gender, search_gender, romance, finance, distance, name):
      self.set_all(gender, search_gender, romance, finance, distance, name)

   # --------------- Accessors -----------------

   # Returns the gender
   def get_gender(self):
      return self.gender

   # Returns the search gender
   def get_search_gender(self):
      return self.search_gender

   # Returns the romance value
   def get_romance(self):
      return self.romance

   # Return the finance value
   def get_finance(self):
      return self.finance

   # Return the distance value
   def get_distance(self):
      return self.distance

   # Return the name
   def get_name(self):
      return self.name

   # --------------- Mutators -----------------

   # Sets the gender. Checks to see if input is valid
   def set_gender(self, gen):
      if self.valid_gender(gen):
         self.gender = gen
         return True
      else:
         return False

   # Sets the search gender. Checks to see if input is valid
   def set_search_gender(self, search_gen):
      if self.valid_gender(search_gen):
         self.search_gender = search_gen
         return True
      else:
         return False

   # Sets the romance value. Checks to see if input is valid
   def set_romance(self, rom):
      if self.valid_number(rom):
         self.romance = rom
         return True
      else:
         return False

   # Sets the finance value. Checks to see if input is valid
   def set_finance(self, fin):
      if self.valid_number(fin):
         self.finance = fin
         return True
      else:
         return False

   # Sets the distance value. Checks to see if input is valid
   def set_distance(self, dist):
      if self.valid_number(dist):
         self.distance = dist
         return True
      else:
         return False

   # Sets the name. Checks to see if input is valid
   def set_name(self, nam):
      if self.valid_string(nam):
         self.name = nam
         return True
      else:
         return False

   # Sets all the object variables to parameter values
   def set_all(self, gend, search_gend, rom, fin, dist, nam):
      if not self.set_gender(gend):
         self.gender = self.DEFAULT_GEND
      if not self.set_search_gender(search_gend):
         self.search_gender = self.DEFAULT_SEARCH_GEND
      if not self.set_romance(rom):
         self.romance = self.DEFAULT_INT
      if not self.set_finance(fin):
         self.finance = self.DEFAULT_INT
      if not self.set_distance(dist):
         self.distance = self.DEFAULT_INT
      if not self.set_name(nam):
         self.name = self.DEFAULT_NAME

   # Sets all the object variables to default values
   def set_defaults(self):
      self.gender = self.DEFAULT_GEND
      self.search_gender = self.DEFAULT_SEARCH_GEND
      self.romance = self.DEFAULT_INT
      self.finance = self.DEFAULT_INT
      self.distance = self.DEFAULT_INT
      self.name = self.DEFAULT_NAME

   # Calculates the fit value between two profiles
   def fit_value(self, partner):
      if self.determine_gender_fit(partner) == 0:
         return 0
      rom_fit = self.determine_romance_fit(partner)
      fin_fit = self.determine_finance_fit(partner)
      dist_fit = self.determine_distance_fit(partner)

      return (rom_fit + fin_fit + dist_fit) / self.NUM_FIT_PARAMS

   # Calculates the gender fit between two profiles
   def determine_gender_fit(self, partner):
      return int(self.search_gender == partner.gender
      and partner.search_gender == self.gender)

   # Calculates the romance fit between two values
   def determine_romance_fit(self, partner):
      return 1.0 - (abs(self.romance - partner.romance) / self.MAX_INT)

   # Calculates the finance fit between two profiles
   def determine_finance_fit(self, partner):
      return 1.0 - (abs(self.finance - partner.finance) / self.MAX_INT)

   # Calculates the distance fit between two profiles
   def determine_distance_fit(self, partner):
      return 1.0 - (abs(self.distance - partner.distance) / self.MAX_INT)

   # Runs the to_string() method
   def __str__(self):
      return self.to_string()

   # Prints out the object
   def to_string(self):
      return self.name + " (" + self.gender + ") searching for " + \
             self.search_gender + " w/fin=" + str(self.finance) + \
             " and rom=" + str(self.romance) + " and dist=" + \
             str(self.distance) + "\n"

   # Checks if the string is within the boundaries for length
   @classmethod
   def valid_string(cls, the_str):
      return cls.MIN_NAME_LEN <= len(the_str) <= cls.MAX_NAME_LEN

   # Checks if the number is within the boundaries
   @classmethod
   def valid_number(cls, the_val):
      return cls.MIN_INT <= the_val <= cls.MAX_INT

   # Checks if the gender is valid
   @staticmethod
   def valid_gender(gen):
      return gen == "M" or gen == "F" or gen == "m" or gen == "f"

# --------------- Client -----------------
# Runs the main method defined above

main()

"""
----PART 1 - NO LISTS:----

Robert Dawson (M) searching for F w/fin=3 and rom=5 and dist=1
Rolanda Perry (F) searching for F w/fin=8 and rom=4 and dist=9
Cheryl Landon (F) searching for M w/fin=1 and rom=10 and dist=1
Denise Deduncan (F) searching for F w/fin=4 and rom=7 and dist=2

Fit between Robert Dawson and Robert Dawson:	0
Fit between Robert Dawson and Rolanda Perry:	0
Fit between Robert Dawson and Cheryl Landon:	0.7666666666666666
Fit between Robert Dawson and Denise Deduncan:	0


Fit between Rolanda Perry and Robert Dawson:	0
Fit between Rolanda Perry and Rolanda Perry:	1.0
Fit between Rolanda Perry and Cheryl Landon:	0
Fit between Rolanda Perry and Denise Deduncan:	0.5333333333333333


Fit between Cheryl Landon and Robert Dawson:	0.7666666666666666
Fit between Cheryl Landon and Rolanda Perry:	0
Fit between Cheryl Landon and Cheryl Landon:	0
Fit between Cheryl Landon and Denise Deduncan:	0


Fit between Denise Deduncan and Robert Dawson:	0
Fit between Denise Deduncan and Rolanda Perry:	0.5333333333333333
Fit between Denise Deduncan and Cheryl Landon:	0
Fit between Denise Deduncan and Denise Deduncan:	1.0

----PART 2 - LIST OF OBJECTS:----

Robert Dawson (M) searching for F w/fin=3 and rom=5 and dist=1

Rolanda Perry (F) searching for F w/fin=8 and rom=4 and dist=9

Cheryl Landon (F) searching for M w/fin=1 and rom=10 and dist=1

Denise Deduncan (F) searching for F w/fin=4 and rom=7 and dist=2

Fit between Robert Dawson and Robert Dawson:	0
Fit between Robert Dawson and Rolanda Perry:	0
Fit between Robert Dawson and Cheryl Landon:	0.7666666666666666
Fit between Robert Dawson and Denise Deduncan:	0


Fit between Rolanda Perry and Robert Dawson:	0
Fit between Rolanda Perry and Rolanda Perry:	1.0
Fit between Rolanda Perry and Cheryl Landon:	0
Fit between Rolanda Perry and Denise Deduncan:	0.5333333333333333


Fit between Cheryl Landon and Robert Dawson:	0.7666666666666666
Fit between Cheryl Landon and Rolanda Perry:	0
Fit between Cheryl Landon and Cheryl Landon:	0
Fit between Cheryl Landon and Denise Deduncan:	0


Fit between Denise Deduncan and Robert Dawson:	0
Fit between Denise Deduncan and Rolanda Perry:	0.5333333333333333
Fit between Denise Deduncan and Cheryl Landon:	0
Fit between Denise Deduncan and Denise Deduncan:	1.0



----PART 3 - USING THE MUTATORS:----


Setting the name of applicant1 to Roger Smith:
Accepted input

Setting the finance of applicant2 to -5:
Invalid input

Setting the gender of applicant3 to m:
Accepted input

Setting the gender of applicant4 to e:
Invalid input

Re-printing mutated applicants: 
Roger Smith (M) searching for F w/fin=3 and rom=5 and dist=1
Rolanda Perry (F) searching for F w/fin=8 and rom=4 and dist=9
Cheryl Landon (m) searching for M w/fin=1 and rom=10 and dist=1
Denise Deduncan (F) searching for F w/fin=4 and rom=7 and dist=2 
"""