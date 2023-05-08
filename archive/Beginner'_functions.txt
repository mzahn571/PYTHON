# Beginner's Python
# Cheat Sheet –
# Functions

# What are functions?
# Functions are named blocks of code designed to do
# one specific job. Functions allow you to write code
# once that can then be run whenever you need to
# accomplish the same task. Functions can take in the
# information they need, and return the information they
# generate. Using functions effectively makes your
# programs easier to write, read, test, and fix.


# Defining a function
# The first line of a function is its definition, marked by the
# keyword def. The name of the function is followed by a set
# of parentheses and a colon. A docstring, in triple quotes,
# describes what the function does. The body of a function is
# indented one level.
# To call a function, give the name of the function followed
# by a set of parentheses.

# Making a function
    def greet_user():
        """Display a simple greeting."""
        print("Hello!")
    
    greet_user()

# Passing information to a function
# Information that's passed to a function is called an
# argument; information that's received by a function is called
# a parameter. Arguments are included in parentheses after
# the function's name, and parameters are listed in
# parentheses in the function's definition.

# Passing a single argument
    def greet_user(username):
        """Display a simple greeting."""
        print(f"Hello, {username}!")
        
    greet_user('jesse')
    greet_user('diana')
    greet_user('brandon')
    
# Positional and keyword arguments
# The two main kinds of arguments are positional and
# keyword arguments. When you use positional arguments
# Python matches the first argument in the function call with
# the first parameter in the function definition, and so forth.
# With keyword arguments, you specify which parameter
# each argument should be assigned to in the function call.
# When you use keyword arguments, the order of the
# arguments doesn't matter.

# Using positional arguments
    def describe_pet(animal, name):
        """Display information about a pet."""
        print(f"\nI have a {animal}.")
        print(f"Its name is {name}.")
    
    describe_pet('hamster', 'harry')
    describe_pet('dog', 'willie')

# Using keyword arguments
    def describe_pet(animal, name):
        """Display information about a pet."""
        print(f"\nI have a {animal}.")
        print(f"Its name is {name}.")
        
    describe_pet(animal='hamster', name='harry')
    describe_pet(name='willie', animal='dog')

# Default values
# You can provide a default value for a parameter. When
# function calls omit this argument the default value will be
# used. Parameters with default values must be listed after
# parameters without default values in the function's definition
# so positional arguments can still work correctly.

# Using a default value
    def describe_pet(name, animal='dog'):
        """Display information about a pet."""
        print(f"\nI have a {animal}.")
        print(f"Its name is {name}.")
    
    describe_pet('harry', 'hamster')
    describe_pet('willie')

# Using None to make an argument optional
    def describe_pet(animal, name=None):
        """Display information about a pet."""
        print(f"\nI have a {animal}.")
        if name:
            print(f"Its name is {name}.")
            
    describe_pet('hamster', 'harry')
    describe_pet('snake')

# Return values
# A function can return a value or a set of values. When a
# function returns a value, the calling line should provide a
# variable which the return value can be assigned to. A
# function stops running when it reaches a return statement.

# Returning a single value
    def get_full_name(first, last):
        """Return a neatly formatted full name."""
        full_name = f"{first} {last}"
        return full_name.title()
        
    musician = get_full_name('jimi', 'hendrix')
    print(musician)

# Returning a dictionary
    def build_person(first, last):
        """Return a dictionary of information
        about a person.
        """
        person = {'first': first, 'last': last}
        return person
        
    musician = build_person('jimi', 'hendrix')
    print(musician)

# Returning a dictionary with optional values
    def build_person(first, last, age=None):
        """Return a dictionary of information
        about a person.
        """
        person = {'first': first, 'last': last}
        if age:
            person['age'] = age
        return person
    
    musician = build_person('jimi', 'hendrix', 27)
    print(musician)
    
    musician = build_person('janis', 'joplin')
    print(musician)

# Passing a list to a function
# You can pass a list as an argument to a function, and the
# function can work with the values in the list. Any changes
# the function makes to the list will affect the original list. You
# can prevent a function from modifying a list by passing a
# copy of the list as an argument.

# Passing a list as an argument
    def greet_users(names):
        """Print a simple greeting to everyone."""
        for name in names:
            msg = f"Hello, {name}!"
            print(msg)
            
    usernames = ['hannah', 'ty', 'margot']
    greet_users(usernames)
    
# Allowing a function to modify a list
# The following example sends a list of models to a function for
# printing. The original list is emptied, and the second list is filled.
    def print_models(unprinted, printed):
        """3d print a set of models."""
        while unprinted:
            current_model = unprinted.pop()
            print(f"Printing {current_model}")
            printed.append(current_model)
            
    # Store some unprinted designs,
    # and print each of them.
    unprinted = ['phone case', 'pendant', 'ring']
    printed = []
    print_models(unprinted, printed)
    
    print(f"\nUnprinted: {unprinted}")
    print(f"Printed: {printed}")
    
# Preventing a function from modifying a list
# The following example is the same as the previous one, except the
# original list is unchanged after calling print_models().
    def print_models(unprinted, printed):
        """3d print a set of models."""
        while unprinted:
            current_model = unprinted.pop()
            print(f"Printing {current_model}")
            printed.append(current_model)

    # Store some unprinted designs,
    # and print each of them.
    original = ['phone case', 'pendant', 'ring']
    printed = []
    
    print_models(original[:], printed)
    print(f"\nOriginal: {original}")
    print(f"Printed: {printed}")
    
# Passing an arbitrary number of arguments
# Sometimes you won't know how many arguments a
# function will need to accept. Python allows you to collect an
# arbitrary number of arguments into one parameter using the
# * operator. A parameter that accepts an arbitrary number of
# arguments must come last in the function definition.
# The ** operator allows a parameter to collect an arbitrary
# number of keyword arguments. These arguments are
# stored as a dictionary with the parameter names as keys,
# and the arguments as values.

# Collecting an arbitrary number of arguments
    def make_pizza(size, *toppings):
        """Make a pizza."""
        print(f"\nMaking a {size} pizza.")
        print("Toppings:")
        for topping in toppings:
            print(f"- {topping}")
            
    # Make three pizzas with different toppings.
    make_pizza('small', 'pepperoni')
    make_pizza('large', 'bacon bits', 'pineapple')
    make_pizza('medium', 'mushrooms', 'peppers',
            'onions', 'extra cheese')
    
# Collecting an arbitrary number of keyword arguments
    def build_profile(first, last, **user_info):
        """Build a dictionary for a user."""
        user_info['first'] = first
        user_info['last'] = last
    
    return user_info
    
    # Create two users with different kinds
    # of information.
    user_0 = build_profile('albert', 'einstein',
            location='princeton')
    
    user_1 = build_profile('marie', 'curie',
            location='paris', field='chemistry')
    
    print(user_0)
    print(user_1)

# Modules
# You can store your functions in a separate file called a
# module, and then import the functions you need into the file
# containing your main program. This allows for cleaner
# program files. (Make sure your module is stored in the
# same directory as your main program.)

# Storing a function in a module
# File: pizza.py
    def make_pizza(size, *toppings):
        """Make a pizza."""
        print(f"\nMaking a {size} pizza.")
        print("Toppings:")
    for topping in toppings:
        print(f"- {topping}")
    
# Importing an entire module
# File: making_pizzas.py
# Every function in the module is available in the program file.
    import pizza
    
    pizza.make_pizza('medium', 'pepperoni')
    pizza.make_pizza('small', 'bacon', 'pineapple')
    
# Importing a specific function
# Only the imported functions are available in the program file.
    from pizza import make_pizza
    
    make_pizza('medium', 'pepperoni')
    make_pizza('small', 'bacon', 'pineapple')
    
# Giving a module an alias
    import pizza as p
    
    p.make_pizza('medium', 'pepperoni')
    p.make_pizza('small', 'bacon', 'pineapple')
    
# Giving a function an alias
    from pizza import make_pizza as mp
    
    mp('medium', 'pepperoni')
    mp('small', 'bacon', 'pineapple')
    
# Importing all functions from a module
# Don't do this, but recognize it when you see it in others' code. It
# can result in naming conflicts, which can cause errors.
    from pizza import *
    
    make_pizza('medium', 'pepperoni')
    make_pizza('small', 'bacon', 'pineapple')
    













































































