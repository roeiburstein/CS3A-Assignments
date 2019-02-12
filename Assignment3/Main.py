# --------------- Source -----------------
#!/usr/bin/env python
__author__ = "Roei Burstein"

import sys

# ------------ food #1 constants -------------
FOOD_1_NAME = "tomato"
FOOD_1_CALORIES_P100G = 18.0  # in calories
FOOD_1_PROTEIN_P100G = 0.9  # in grams
FOOD_1_VITAMIN_C_P100G = 12.7 # in milligrams
FOOD_1_POTASSIUM_P100G = 237.0 # in milligrams
FOOD_1_CALCIUM_P100G = 10.0 # in milligrams
FOOD_1_MAGNESIUM_P100G = 11.0 # in milligrams

# ------------ food #2 constants ------------
FOOD_2_NAME = "cucumbers"
FOOD_2_CALORIES_P100G = 15.0  # in calories
FOOD_2_PROTEIN_P100G = 0.7  # in grams
FOOD_2_VITAMIN_C_P100G = 2.8 # in milligrams
FOOD_2_POTASSIUM_P100G = 147.0 # in milligrams
FOOD_2_CALCIUM_P100G = 16.0 # in milligrams
FOOD_2_MAGNESIUM_P100G = 13.0 # in milligrams

# ------------ food #3 constants ------------
FOOD_3_NAME = "spinach"
FOOD_3_CALORIES_P100G = 23.0  # in calories
FOOD_3_PROTEIN_P100G = 2.9  # in grams
FOOD_3_VITAMIN_C_P100G = 28.1 # in milligrams
FOOD_3_POTASSIUM_P100G = 558.0 # in milligrams
FOOD_3_CALCIUM_P100G = 99.0 # in milligrams
FOOD_3_MAGNESIUM_P100G = 79.0 # in milligrams

# ------------ food #4 constants ------------
FOOD_4_NAME = "feta cheese"
FOOD_4_CALORIES_P100G = 264.0  # in calories
FOOD_4_PROTEIN_P100G = 14.2  # in grams
FOOD_4_VITAMIN_C_P100G = 0.0 # in milligrams
FOOD_4_POTASSIUM_P100G = 62.0 # in milligrams
FOOD_4_CALCIUM_P100G = 493.0 # in milligrams
FOOD_4_MAGNESIUM_P100G = 0.0 # in milligrams

# ------------ food #5 constants ------------
FOOD_5_NAME = "broccoli"
FOOD_5_CALORIES_P100G = 34.0  # in calories
FOOD_5_PROTEIN_P100G = 2.8  # in grams
FOOD_5_VITAMIN_C_P100G = 89.2 # in milligrams
FOOD_5_POTASSIUM_P100G = 316.0 # in milligrams
FOOD_5_CALCIUM_P100G = 47.0 # in milligrams
FOOD_5_MAGNESIUM_P100G = 21.0 # in milligrams

# ------------ food #6 constants ------------
FOOD_6_NAME = "bell peppers"
FOOD_6_CALORIES_P100G = 20.0  # in calories
FOOD_6_PROTEIN_P100G = 0.9  # in grams
FOOD_6_VITAMIN_C_P100G = 80.4 # in milligrams
FOOD_6_POTASSIUM_P100G = 175.0 # in milligrams
FOOD_6_CALCIUM_P100G = 10.0 # in milligrams
FOOD_6_MAGNESIUM_P100G = 10.0 # in milligrams
INDENT = "   "

# ------------ limit constants -------------
MIN_SERVINGS = 1
MAX_SERVINGS = 15
MIN_GRAMS = 0
MAX_GRAMS = 1500

# initialize variables
total_cals = 0
total_protein = 0
total_vitamin_c = 0
total_potassium = 0
total_calcium = 0
total_magnesium = 0

# print menu items
print("---------- List of Possible Ingredients ---------")
print(INDENT + "Food #1: " + FOOD_1_NAME)
print(INDENT + "Food #2: " + FOOD_2_NAME)
print(INDENT + "Food #3: " + FOOD_3_NAME)
print(INDENT + "Food #4: " + FOOD_4_NAME)
print(INDENT + "Food #5: " + FOOD_5_NAME)
print(INDENT + "Food #6: " + FOOD_6_NAME + "\n")

# recipe name
recipe_name = input("Name of your recipe: ")
num_servings = int(input("Number of servings: "))

if (num_servings < MIN_SERVINGS) or (num_servings > MAX_SERVINGS):
   print("ERROR: invalid number of servings (must be between "
   + str(MIN_SERVINGS) + " and " + str(MAX_SERVINGS) + ")")
   sys.exit()

# food #1 ---------------------------------------------------------
user_input_int = int(input(INDENT + "How many grams of " + FOOD_1_NAME + "? "))

if (user_input_int < MIN_GRAMS) or (user_input_int > MAX_GRAMS):
   print("ERROR: invalid number of grams (must be between "
   + str(MIN_GRAMS) + " and " + str(MAX_GRAMS) + ")")
   sys.exit()

# update accumulators
total_cals += user_input_int * (FOOD_1_CALORIES_P100G / 100.)
total_protein += user_input_int * (FOOD_1_PROTEIN_P100G / 100.)
total_vitamin_c += user_input_int * (FOOD_1_VITAMIN_C_P100G / 100.)
total_potassium += user_input_int * (FOOD_1_POTASSIUM_P100G / 100.)
total_calcium += user_input_int * (FOOD_1_CALCIUM_P100G / 100.)
total_magnesium += user_input_int * (FOOD_1_MAGNESIUM_P100G / 100.)


# food #2 ---------------------------------------------------------
user_input_int = int(input(INDENT + "How many grams of " + FOOD_2_NAME + "? "))

if (user_input_int < MIN_GRAMS) or (user_input_int > MAX_GRAMS):
   print("ERROR: invalid number of grams (must be between "
         + str(MIN_GRAMS) + " and " + str(MAX_GRAMS) + ")")
   sys.exit()

# update accumulators
total_cals += user_input_int * (FOOD_2_CALORIES_P100G / 100.)
total_protein += user_input_int * (FOOD_2_PROTEIN_P100G / 100.)
total_vitamin_c += user_input_int * (FOOD_2_VITAMIN_C_P100G / 100.)
total_potassium += user_input_int * (FOOD_2_POTASSIUM_P100G / 100.)
total_calcium += user_input_int * (FOOD_2_CALCIUM_P100G / 100.)
total_magnesium += user_input_int * (FOOD_2_MAGNESIUM_P100G / 100.)

# food #3 ---------------------------------------------------------
user_input_int = int(input(INDENT + "How many grams of " + FOOD_3_NAME + "? "))

if (user_input_int < MIN_GRAMS) or (user_input_int > MAX_GRAMS):
   print("ERROR: invalid number of grams (must be between "
         + str(MIN_GRAMS) + " and " + str(MAX_GRAMS) + ")")
   sys.exit()

# update accumulators
total_cals += user_input_int * (FOOD_3_CALORIES_P100G / 100.)
total_protein += user_input_int * (FOOD_3_PROTEIN_P100G / 100.)
total_vitamin_c += user_input_int * (FOOD_3_VITAMIN_C_P100G / 100.)
total_potassium += user_input_int * (FOOD_3_POTASSIUM_P100G / 100.)
total_calcium += user_input_int * (FOOD_3_CALCIUM_P100G / 100.)
total_magnesium += user_input_int * (FOOD_3_MAGNESIUM_P100G / 100.)

# food #4 ---------------------------------------------------------
user_input_int = int(input(INDENT + "How many grams of " + FOOD_4_NAME + "? "))

if (user_input_int < MIN_GRAMS) or (user_input_int > MAX_GRAMS):
   print("ERROR: invalid number of grams (must be between "
         + str(MIN_GRAMS) + " and " + str(MAX_GRAMS) + ")")
   sys.exit()

# update accumulators
total_cals += user_input_int * (FOOD_4_CALORIES_P100G / 100.)
total_protein += user_input_int * (FOOD_4_PROTEIN_P100G / 100.)
total_vitamin_c += user_input_int * (FOOD_4_VITAMIN_C_P100G / 100.)
total_potassium += user_input_int * (FOOD_4_POTASSIUM_P100G / 100.)
total_calcium += user_input_int * (FOOD_4_CALCIUM_P100G / 100.)
total_magnesium += user_input_int * (FOOD_4_MAGNESIUM_P100G / 100.)

# food #5 ---------------------------------------------------------
user_input_int = int(input(INDENT + "How many grams of " + FOOD_5_NAME + "? "))

if (user_input_int < MIN_GRAMS) or (user_input_int > MAX_GRAMS):
   print("ERROR: invalid number of grams (must be between "
         + str(MIN_GRAMS) + " and " + str(MAX_GRAMS) + ")")
   sys.exit()

# update accumulators
total_cals += user_input_int * (FOOD_5_CALORIES_P100G / 100.)
total_protein += user_input_int * (FOOD_5_PROTEIN_P100G / 100.)
total_vitamin_c += user_input_int * (FOOD_5_VITAMIN_C_P100G / 100.)
total_potassium += user_input_int * (FOOD_5_POTASSIUM_P100G / 100.)
total_calcium += user_input_int * (FOOD_5_CALCIUM_P100G / 100.)
total_magnesium += user_input_int * (FOOD_5_MAGNESIUM_P100G / 100.)

# food #6 ---------------------------------------------------------
user_input_int = int(input(INDENT + "How many grams of " + FOOD_6_NAME + "? "))

if (user_input_int < MIN_GRAMS) or (user_input_int > MAX_GRAMS):
   print("ERROR: invalid number of grams (must be between "
         + str(MIN_GRAMS) + " and " + str(MAX_GRAMS) + ")")
   sys.exit()

# update accumulators
total_cals += user_input_int * (FOOD_6_CALORIES_P100G / 100.)
total_protein += user_input_int * (FOOD_6_PROTEIN_P100G / 100.)
total_vitamin_c += user_input_int * (FOOD_6_VITAMIN_C_P100G / 100.)
total_potassium += user_input_int * (FOOD_6_POTASSIUM_P100G / 100.)
total_calcium += user_input_int * (FOOD_6_CALCIUM_P100G / 100.)
total_magnesium += user_input_int * (FOOD_6_MAGNESIUM_P100G / 100.)

serving_cals = total_cals/num_servings
serving_protein = total_protein/num_servings
serving_vitamin_c = total_vitamin_c/num_servings
serving_potassium = total_potassium/num_servings
serving_calcium = total_calcium/num_servings
serving_magnesium = total_magnesium/num_servings

# print results --------------------------------------------------
print("\nNutritional value per serving for " + recipe_name + " is:")
print(INDENT + "Calories: " + str(serving_cals))
print(INDENT + "Protein: " + str(serving_protein) + " grams")
print(INDENT + "Vitamin C: " + str(serving_vitamin_c) + " milligrams")
print(INDENT + "Potassium: " + str(serving_potassium) + " milligrams")
print(INDENT + "Calcium: " + str(serving_calcium) + " milligrams")
print(INDENT + "Magnesium: " + str(serving_magnesium) + " milligrams\n")
print()

""" --------------- RUNS -----------------

---------- List of Possible Ingredients ---------
   Food #1: tomato
   Food #2: cucumbers
   Food #3: spinach
   Food #4: feta cheese
   Food #5: broccoli
   Food #6: bell peppers

Name of your recipe: Roei's First Salad
Number of servings: 5
   How many grams of tomato? 80
   How many grams of cucumbers? 40
   How many grams of spinach? 0
   How many grams of feta cheese? 0
   How many grams of broccoli? 0
   How many grams of bell peppers? 0

Nutritional value per serving for Roei's First Salad is:
   Calories: 4.08
   Protein: 0.2 grams
   Vitamin C: 2.256 milligrams
   Potassium: 49.68000000000001 milligrams
   Calcium: 2.88 milligrams
   Magnesium: 2.8 milligrams



Process finished with exit code 0


---------- List of Possible Ingredients ---------
   Food #1: tomato
   Food #2: cucumbers
   Food #3: spinach
   Food #4: feta cheese
   Food #5: broccoli
   Food #6: bell peppers

Name of your recipe: Roei's Second Salad
Number of servings: 1
   How many grams of tomato? 1300
   How many grams of cucumbers? 400
   How many grams of spinach? 900
   How many grams of feta cheese? 1200
   How many grams of broccoli? 800
   How many grams of bell peppers? 659

Nutritional value per serving for Roei's Second Salad is:
   Calories: 4072.8
   Protein: 239.331 grams
   Vitamin C: 1672.6360000000002 milligrams
   Potassium: 13116.25 milligrams
   Calcium: 7442.9 milligrams
   Magnesium: 1139.9 milligrams



Process finished with exit code 0


---------- List of Possible Ingredients ---------
   Food #1: tomato
   Food #2: cucumbers
   Food #3: spinach
   Food #4: feta cheese
   Food #5: broccoli
   Food #6: bell peppers

Name of your recipe: Roei's Third Salad
Number of servings: -3
ERROR: invalid number of servings (must be between 1 and 15)

Process finished with exit code 0



---------- List of Possible Ingredients ---------
   Food #1: tomato
   Food #2: cucumbers
   Food #3: spinach
   Food #4: feta cheese
   Food #5: broccoli
   Food #6: bell peppers

Name of your recipe: Roei's Fourth Salad
Number of servings: 15
   How many grams of tomato? 1
   How many grams of cucumbers? 2
   How many grams of spinach? 3
   How many grams of feta cheese? 4
   How many grams of broccoli? 5
   How many grams of bell peppers? 6

Nutritional value per serving for Roei's Fourth Salad is:
   Calories: 0.9753333333333333
   Protein: 0.058133333333333335 grams
   Vitamin C: 0.6873333333333332 milligrams
   Potassium: 3.388666666666667 milligrams
   Calcium: 1.7373333333333334 milligrams
   Magnesium: 0.2926666666666667 milligrams



Process finished with exit code 0



---------- List of Possible Ingredients ---------
   Food #1: tomato
   Food #2: cucumbers
   Food #3: spinach
   Food #4: feta cheese
   Food #5: broccoli
   Food #6: bell peppers

Name of your recipe: Roei's Fifth Salad
Number of servings: 8
   How many grams of tomato? 300
   How many grams of cucumbers? 250
   How many grams of spinach? 400
   How many grams of feta cheese? 0
   How many grams of broccoli? 0
   How many grams of bell peppers? 280

Nutritional value per serving for Roei's Fifth Salad is:
   Calories: 29.9375
   Protein: 2.32125 grams
   Vitamin C: 47.8275 milligrams
   Potassium: 475.0625 milligrams
   Calcium: 61.75 milligrams
   Magnesium: 51.1875 milligrams



Process finished with exit code 0
-------------------------------------- """
