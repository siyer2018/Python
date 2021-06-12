###########################################################################
### COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###            Assignment 1: Student Introduction (in Python!)          ###
###########################################################################

# Instructions:
# 1. Run the program "as is"
# 2. Save a copy with your FAU username + the '.py' extension
# 3. Modify the code to reflect your name, major, gpa, and hobbies
# 4. Debug and test your code
# 5. Once it's working as intended, submit your .py file via Canvas
# 6. (BONUS) Post your code on a shareable Jupyter site (e.g., Google Colab [1] 
# or Binder [2]) and submit the URl via Canvas

# [1] https://colab.research.google.com/notebooks/intro.ipynb 
# [2] https://github.com/alan-turing-institute/the-turing-way/blob/master/workshops/boost-research-reproducibility-binder/workshop-presentations/zero-to-binder-python.md

###########################################################################

name = "Sharmada Iyer"
academic_status = {"major": "Computer Engineering", "gpa": 3.5}
hobbies = ['video games', 'playing guitar', 'listening to music']

likes = "My hobbies are: \n"
for hobby in hobbies:
    likes = likes + hobby + "\n"

if academic_status['gpa'] == 4.0:
    rating = "perfect"
elif  academic_status['gpa'] >= 3.0:
    rating = "very good"
else:
    rating = "not-so-good"

print(f"My name is {name} \n")
print(f"I am majoring in {academic_status['major']} and my GPA is {academic_status['gpa']}, which is considered {rating}\n")
print(likes)