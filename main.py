# List of all possible anniversary combinations that fulfill the objective 
# (a 3-digit anniversary composed of two 2-digit anniversaries)
wanted_anniversary_combinations = []

age_person_1 = int(input("How old is the first person?\n"))
age_person_2 = int(input("How old is the second person?\n"))

# Get the age difference
age_difference = abs(age_person_1 - age_person_2)

# Get the youngest age to determine when the possible combinations start
youngest_age = age_person_1 if age_person_1 < age_person_2 else age_person_2

# Get the list of all possible combinations
all_age_combinations = list(range(youngest_age * 10, 999))

# Determine which column should print the first person's age 
# (1 - first person is younger | 2 - first person is older)
first_print_column = 1 if age_person_1 == youngest_age else 2

for combination in all_age_combinations:
    age_1 = combination // 10  # Get the first 2 digits
    age_2 = combination % 100  # Get the last 2 digits
    
    # Ensure both ages are at least the youngest age and the age difference is correct
    if abs(age_1 - age_2) == age_difference and age_1 >= youngest_age and age_2 >= youngest_age:
        if first_print_column == 1:
            if age_1 < age_2:
                x, y = age_1, age_2
            else:
                x, y = age_2, age_1
        else:
            if age_1 > age_2:
                x, y = age_1, age_2
            else:
                x, y = age_2, age_1
        wanted_anniversary_combinations.append((x, y, combination))

# Just for better visualization: 
# The first column is the first person's age, the second column is the second person's age, 
# and the third column is the combination
for i in wanted_anniversary_combinations:
    print(i)
