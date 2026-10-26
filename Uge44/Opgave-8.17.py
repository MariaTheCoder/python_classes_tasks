# 8-17. Styling Functions: Choose any three programs you wrote for this chapter,
# and make sure they follow the styling guidelines described in this section.

# def function_name(parameter_0, parameter_1='default value')

# function_name(value_0, parameter_1='value')
from printing_functions import print_models

print_models(["", "", "", "", ""])

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


# def function_name(
# parameter_0, parameter_1, parameter_2,
# parameter_3, parameter_4, parameter_5):
# function body...

def build_profile(first, last, **user_info):
    # Build a dictionary containing everything we know about a user.
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'Maria', 'Andersen', location='Esbjerg',
    field='Cyber Security', email='fake@email.org')
print(user_profile)
