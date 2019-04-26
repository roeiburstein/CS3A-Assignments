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
   MAX_STUDENTS = 20

   num_students = 0
   the_array = []

   # Adds student into array
   def add_student(self, stud):
      if self.num_students < self.MAX_STUDENTS:
         self.the_array.append(stud)
         self.num_students += 1
         return True

      return False

   # Removes student from array. Returns student removed.
   def remove_student(self):
      if self.num_students > 0:
         student = self.the_array[self.num_students - 1]
         self.the_array.pop()
         self.num_students -= 1
         return student

      return None

   # Sets up the array of students for printing
   def __str__(self, optional_title="--- The Students -----------:\n"):
      return(self.to_string(optional_title))

   # Sorts the array
   def array_sort(self):
      for k in range(self.num_students):
         if not self.float_largest_to_top(self.num_students - k):
            return

   # Gets the median total points for the array
   def get_median_destructive(self):
      if(self.num_students < 1):
         return 0

      old_sort_key = Student.get_sort_key()
      Student.set_sort_key(Student.SORT_BY_POINTS)
      self.array_sort()
      median = -1

      if(self.num_students % 2 == 0):
         median = (self.the_array[(self.num_students // 2)
         - 1].get_total_points() +
         self.the_array[self.num_students // 2].get_total_points()) / 2

      else:
         median = self.the_array[self.num_students // 2].get_total_points()

      Student.set_sort_key(old_sort_key)
      return median

   # Sets up student array for printing
   def to_string(self, optional_title="--- The Students -----------:\n"):
      ret_val = optional_title + "\n"
      for student in self.the_array:
         ret_val = ret_val + str(student) + "\n"
      return ret_val

   def float_largest_to_top(self, top):

      changed = False

      # notice we stop at num_students - 2 because of expr. k + 1 in loop
      for k in range(top - 1):
         if Student.compare_two_students(
            self.the_array[k], self.the_array[k + 1]) > 0:
            self.the_array[k], self.the_array[k + 1] = self.the_array[k + 1], \
                                                       self.the_array[k]
            changed = True

      return changed


# client --------------------------------------------

# instantiate some students, one with an illegal name ...
my_class = \
   [
   Student("smith","fred", 95),
   Student("bauer","jack",123),
   Student("jacobs","carrie", 195),  Student("renquist","abe",148),
   Student("3ackson","trevor", 108),  Student("perry","fred",225),
   Student("loceff","fred", 44),  Student("stollings","pamela",452),
   Student("charters","rodney", 295),  Student("cassar","john",321)
   ]

array_size = len(my_class)

# instantiate an SAU object
my_studs = StudentArrayUtilities()

# we can add students manually and individually
my_studs.add_student( Student( "bartman", "petra", 102 ) )
my_studs.add_student( Student( "charters", "rodney", 295 ) )

# if we happen to have an array available, we can add students in loop
for k in range(array_size):
   my_studs.add_student(my_class[k])

print( "Before sorting:\n\n" + str(my_studs) )
my_studs.array_sort()
print( "After default sort (LAST):\n\n" + str(my_studs) )

Student.set_sort_key(Student.SORT_BY_FIRST)
my_studs.array_sort()
print( "After dsort by FIRST\n\n:" + str(my_studs) )

# test median
med = my_studs.get_median_destructive()
print( "Median of even class =", med)
if Student.get_sort_key() == Student.SORT_BY_FIRST:
   print( "Successfully preserved sort key." )
else:
   print( " ** problem **" )

# various tests of removing and adding too many students
for k in range(100):
   student = my_studs.remove_student()
   if student != None:
      print( "Removed " + str(student) )
   else:
      print( "Empty after", k, "removes." )
      break

for k in range(100):
   if not my_studs.add_student(Student("first", "last", 22)):
      print( "Full after", k, "adds."  )
      break
   else:
      print( "Added(first, last, 22)" )
"""
Before sorting:

--- The Students -----------:

 ---------- 
    name: bartman, petra
    total points: 102.
 ---------- 
    name: charters, rodney
    total points: 295.
 ---------- 
    name: smith, fred
    total points: 95.
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: renquist, abe
    total points: 148.
 ---------- 
    name: zz-error, trevor
    total points: 108.
 ---------- 
    name: perry, fred
    total points: 225.
 ---------- 
    name: loceff, fred
    total points: 44.
 ---------- 
    name: stollings, pamela
    total points: 452.
 ---------- 
    name: charters, rodney
    total points: 295.
 ---------- 
    name: cassar, john
    total points: 321.

After default sort (LAST):

--- The Students -----------:

 ---------- 
    name: bartman, petra
    total points: 102.
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: cassar, john
    total points: 321.
 ---------- 
    name: charters, rodney
    total points: 295.
 ---------- 
    name: charters, rodney
    total points: 295.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: loceff, fred
    total points: 44.
 ---------- 
    name: perry, fred
    total points: 225.
 ---------- 
    name: renquist, abe
    total points: 148.
 ---------- 
    name: smith, fred
    total points: 95.
 ---------- 
    name: stollings, pamela
    total points: 452.
 ---------- 
    name: zz-error, trevor
    total points: 108.

After dsort by FIRST

:--- The Students -----------:

 ---------- 
    name: renquist, abe
    total points: 148.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: loceff, fred
    total points: 44.
 ---------- 
    name: perry, fred
    total points: 225.
 ---------- 
    name: smith, fred
    total points: 95.
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: cassar, john
    total points: 321.
 ---------- 
    name: stollings, pamela
    total points: 452.
 ---------- 
    name: bartman, petra
    total points: 102.
 ---------- 
    name: charters, rodney
    total points: 295.
 ---------- 
    name: charters, rodney
    total points: 295.
 ---------- 
    name: zz-error, trevor
    total points: 108.

Median of even class = 171.5
Successfully preserved sort key.
Removed  ---------- 
    name: stollings, pamela
    total points: 452.
Removed  ---------- 
    name: cassar, john
    total points: 321.
Removed  ---------- 
    name: charters, rodney
    total points: 295.
Removed  ---------- 
    name: charters, rodney
    total points: 295.
Removed  ---------- 
    name: perry, fred
    total points: 225.
Removed  ---------- 
    name: jacobs, carrie
    total points: 195.
Removed  ---------- 
    name: renquist, abe
    total points: 148.
Removed  ---------- 
    name: bauer, jack
    total points: 123.
Removed  ---------- 
    name: zz-error, trevor
    total points: 108.
Removed  ---------- 
    name: bartman, petra
    total points: 102.
Removed  ---------- 
    name: smith, fred
    total points: 95.
Removed  ---------- 
    name: loceff, fred
    total points: 44.
Empty after 12 removes.
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Added(first, last, 22)
Full after 20 adds.

"""