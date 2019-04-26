# --------------- Source -----------------

#!/usr/bin/env python
__author__ = "Roei Burstein"

""" This program creates student objects with first names, last names, and
scores. We created sorts for each attribute of the object, and arrays
containing different quantities of students. We then found the median score of
each list of students.
"""

# beginning of class Student definition -------------------------
class Student:
   # class ("static") attributes and intended constants
   DEFAULT_NAME = "zz-error"
   DEFAULT_POINTS = 0
   MAX_POINTS = 1000
   SORT_BY_FIRST = 88
   SORT_BY_LAST = 98
   SORT_BY_POINTS = 108
   sort_key = SORT_BY_LAST

   # initializer ("constructor") method -------------------
   def __init__(self,
                last=DEFAULT_NAME,
                first=DEFAULT_NAME,
                points=DEFAULT_POINTS):
      # instance attributes
      if (not self.set_last_name(last)):
         self.last_name = Student.DEFAULT_NAME
      if (not self.set_first_name(first)):
         self.first_name = Student.DEFAULT_NAME
      if (not self.set_points(points)):
         self.total_points = Student.DEFAULT_POINTS

   # mutator ("set") methods -------------------------------

   # Setter for the last name parameter
   def set_last_name(self, last):
      if not self.valid_string(last):
         return False
      # else
      self.last_name = last
      return True

   # Setter for the first name parameter
   def set_first_name(self, first):
      if not self.valid_string(first):
         return False
      # else
      self.first_name = first
      return True

   # Setter for the points parameter
   def set_points(self, points):
      if not self.valid_points(points):
         return False
      # else
      self.total_points = points
      return True

   # Sets the sort key to sort by first name, last name, or points
   @classmethod
   def set_sort_key(cls, key):
      cls.sort_key = key

   # accessor ("get") methods -------------------------------

   # Getter for the last name parameter
   def get_last_name(self):
      return self.last_name

   # Getter for the first name parameter
   def get_first_name(self):
      return self.first_name

   # Getter for the total points parameter
   def get_total_points(self):
      return self.total_points

   # Gets an integer representation for the sort key
   @classmethod
   def get_sort_key(cls):
      return cls.sort_key

   # output method  ----------------------------------------
   def display(self, client_intro_str="--- STUDENT DATA ---"):
      print(client_intro_str + str(self))

   # standard python stringizer ------------------------
   def __str__(self):
      return self.to_string()

   # instance helpers -------------------------------

   # Formats the string for printing
   def to_string(self, optional_title=" ---------- "):
      ret_str = ((optional_title
                  + "\n    name: {}, {}"
                  + "\n    total points: {}.").
                 format(self.last_name, self.first_name,
                        self.total_points))
      return ret_str

   # static/class methods -----------------------------------

   # Checks if the string is within the parameters
   @staticmethod
   def valid_string(test_str):
      if (len(test_str) > 0) and test_str[0].isalpha():
         return True;
      return False

   # Checks if the number of points is within the parameters
   @classmethod
   def valid_points(cls, test_points):
      if 0 <= test_points <= cls.MAX_POINTS:
         return True
      else:
         return False

   # Compares two strings based on alphabetical order
   @staticmethod
   def compare_strings_ignore_case(first_string, second_string):
      """ returns -1 if first < second, lexicographically,
         +1 if first > second, and 0 if same
         this particular version based on the first or last name
         (case insensitive) """

      fst_upper = first_string.upper()
      scnd_upper = second_string.upper()
      if fst_upper < scnd_upper:
         return -1
      # else if
      if fst_upper > scnd_upper:
         return 1
      # else
      return 0

   # Compares two students based on the sort key
   @classmethod
   def compare_two_students(cls, first_stud, second_stud):
      if(cls.sort_key == cls.SORT_BY_FIRST):
         return cls.compare_strings_ignore_case(first_stud.first_name,
                                                second_stud.first_name)

      elif(cls.sort_key == cls.SORT_BY_LAST):
         return cls.compare_strings_ignore_case(first_stud.last_name,
                                                second_stud.last_name)

      else:
         return first_stud.total_points - second_stud.total_points

# beginning of class StudentArrayUtilities definition ---------------
class StudentArrayUtilities:

   # Sets up the array of students for printing
   @classmethod
   def to_string(cls, stud_array,
                   optional_title="--- The Students -----------:\n"):
      return(cls.to_string(stud_array, optional_title))

   # Sorts the array
   @classmethod
   def array_sort(cls, data, array_size):
      for k in range(array_size):
         if not cls.float_largest_to_top(data, array_size - k):
            return

   # Gets the median total points for the array
   @classmethod
   def get_median_destructive(cls, array, array_size):
      if(array_size < 1):
         return 0

      old_sort_key = Student.get_sort_key()
      Student.set_sort_key(Student.SORT_BY_POINTS)
      cls.array_sort(array, array_size)
      median = -1

      if(array_size % 2 == 0):
         median = (array[(array_size // 2) - 1].get_total_points()\
         + array[array_size // 2].get_total_points()) / 2

      else:
         median = array[array_size // 2].get_total_points()

      Student.set_sort_key(old_sort_key)
      return median

            # class stringizers ----------------------------------

   # Sets up student array for printing
   @staticmethod
   def to_string(stud_array,
                 optional_title="--- The Students -----------:\n"):
      ret_val = optional_title + "\n"
      for student in stud_array:
         ret_val = ret_val + str(student) + "\n"
      return ret_val

   @staticmethod
   def float_largest_to_top(data, array_size):

      changed = False

      # notice we stop at array_size - 2 because of expr. k + 1 in loop
      for k in range(array_size - 1):
         if Student.compare_two_students(data[k], data[k + 1]) > 0:
            data[k], data[k + 1] = data[k + 1], data[k]
            changed = True

      return changed


# client --------------------------------------------

# instantiate some students, one with and illegal name ...
student_array_1 = \
   [
      Student("Curry", "Stephen", 53),
      Student("Thompson", "Klay", 72),
      Student("durant", "Kevin", 89),
      Student("Cousins", "deMarcus", 148),
      Student("3ogut", "Andrew", 102),
      Student("green", "draymond", 63),
      Student("iguodala", "Andre", 99),
      Student("mcKinnie", "Alfonzo", 295),
      Student("Bell", "jordan", 236),
      Student("looney", "Kevon", 452),
      Student("Jones", "Damian", 74),
      Student("Cook", "Quinn", 220),
      Student("evans", "Jacob", 145),
      Student("derrickson", "Marcus", 452),
      Student("Jerebko", "Jonas", 840)
   ]

student_array_2 = student_array_1[:]
student_array_2.append(Student("Kerr", "Steve", 80))

student_array_3 = [Student("Burstein", "Roei", 100)]

# Printing original array
print(StudentArrayUtilities.to_string(student_array_2,
                                      "Before default sort (even):"))

# Sorting by default
StudentArrayUtilities.array_sort(student_array_2, len(student_array_2))
print(StudentArrayUtilities.to_string(student_array_2,
                                      "After default sort (even):"))

# Sorting by first name
Student.set_sort_key(Student.SORT_BY_FIRST)
StudentArrayUtilities.array_sort(student_array_2, len(student_array_2))
print(StudentArrayUtilities.to_string(student_array_2,
                                      "After sort BY FIRST:"))

# Sorting by points
Student.set_sort_key(Student.SORT_BY_POINTS)
StudentArrayUtilities.array_sort(student_array_2, len(student_array_2))
print(StudentArrayUtilities.to_string(student_array_2,
                                      "After sort BY POINTS:"))

# Getting median of student_array_2
Student.set_sort_key(Student.SORT_BY_FIRST)
print("\nMedian of even class: ")
print(StudentArrayUtilities.get_median_destructive(student_array_2,
                                             len(student_array_2)))

# Printing original sort key
print("\nChecking sort key. Should be 88 for first name sort:")
print(Student.get_sort_key())

# Getting median of student_array_1
print("\nMedian of odd class: ")
print(StudentArrayUtilities.get_median_destructive(student_array_1,
                                             len(student_array_1)))

# Getting median of student_array_3
print("\nMedian of small class: ")
print(StudentArrayUtilities.get_median_destructive(student_array_3,
                                             len(student_array_3)))

"""
Before default sort (even):
 ---------- 
    name: Curry, Stephen
    total points: 53.
 ---------- 
    name: Thompson, Klay
    total points: 72.
 ---------- 
    name: durant, Kevin
    total points: 89.
 ---------- 
    name: Cousins, deMarcus
    total points: 148.
 ---------- 
    name: zz-error, Andrew
    total points: 102.
 ---------- 
    name: green, draymond
    total points: 63.
 ---------- 
    name: iguodala, Andre
    total points: 99.
 ---------- 
    name: mcKinnie, Alfonzo
    total points: 295.
 ---------- 
    name: Bell, jordan
    total points: 236.
 ---------- 
    name: looney, Kevon
    total points: 452.
 ---------- 
    name: Jones, Damian
    total points: 74.
 ---------- 
    name: Cook, Quinn
    total points: 220.
 ---------- 
    name: evans, Jacob
    total points: 145.
 ---------- 
    name: derrickson, Marcus
    total points: 452.
 ---------- 
    name: Jerebko, Jonas
    total points: 840.
 ---------- 
    name: Kerr, Steve
    total points: 80.

After default sort (even):
 ---------- 
    name: Bell, jordan
    total points: 236.
 ---------- 
    name: Cook, Quinn
    total points: 220.
 ---------- 
    name: Cousins, deMarcus
    total points: 148.
 ---------- 
    name: Curry, Stephen
    total points: 53.
 ---------- 
    name: derrickson, Marcus
    total points: 452.
 ---------- 
    name: durant, Kevin
    total points: 89.
 ---------- 
    name: evans, Jacob
    total points: 145.
 ---------- 
    name: green, draymond
    total points: 63.
 ---------- 
    name: iguodala, Andre
    total points: 99.
 ---------- 
    name: Jerebko, Jonas
    total points: 840.
 ---------- 
    name: Jones, Damian
    total points: 74.
 ---------- 
    name: Kerr, Steve
    total points: 80.
 ---------- 
    name: looney, Kevon
    total points: 452.
 ---------- 
    name: mcKinnie, Alfonzo
    total points: 295.
 ---------- 
    name: Thompson, Klay
    total points: 72.
 ---------- 
    name: zz-error, Andrew
    total points: 102.

After sort BY FIRST:
 ---------- 
    name: mcKinnie, Alfonzo
    total points: 295.
 ---------- 
    name: iguodala, Andre
    total points: 99.
 ---------- 
    name: zz-error, Andrew
    total points: 102.
 ---------- 
    name: Jones, Damian
    total points: 74.
 ---------- 
    name: Cousins, deMarcus
    total points: 148.
 ---------- 
    name: green, draymond
    total points: 63.
 ---------- 
    name: evans, Jacob
    total points: 145.
 ---------- 
    name: Jerebko, Jonas
    total points: 840.
 ---------- 
    name: Bell, jordan
    total points: 236.
 ---------- 
    name: durant, Kevin
    total points: 89.
 ---------- 
    name: looney, Kevon
    total points: 452.
 ---------- 
    name: Thompson, Klay
    total points: 72.
 ---------- 
    name: derrickson, Marcus
    total points: 452.
 ---------- 
    name: Cook, Quinn
    total points: 220.
 ---------- 
    name: Curry, Stephen
    total points: 53.
 ---------- 
    name: Kerr, Steve
    total points: 80.

After sort BY POINTS:
 ---------- 
    name: Curry, Stephen
    total points: 53.
 ---------- 
    name: green, draymond
    total points: 63.
 ---------- 
    name: Thompson, Klay
    total points: 72.
 ---------- 
    name: Jones, Damian
    total points: 74.
 ---------- 
    name: Kerr, Steve
    total points: 80.
 ---------- 
    name: durant, Kevin
    total points: 89.
 ---------- 
    name: iguodala, Andre
    total points: 99.
 ---------- 
    name: zz-error, Andrew
    total points: 102.
 ---------- 
    name: evans, Jacob
    total points: 145.
 ---------- 
    name: Cousins, deMarcus
    total points: 148.
 ---------- 
    name: Cook, Quinn
    total points: 220.
 ---------- 
    name: Bell, jordan
    total points: 236.
 ---------- 
    name: mcKinnie, Alfonzo
    total points: 295.
 ---------- 
    name: looney, Kevon
    total points: 452.
 ---------- 
    name: derrickson, Marcus
    total points: 452.
 ---------- 
    name: Jerebko, Jonas
    total points: 840.


Median of even class: 
123.5

Checking sort key. Should be 88 for first name sort:
88

Median of odd class: 
145

Median of small class: 
100
"""