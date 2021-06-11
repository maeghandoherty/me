"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this makes a list
some_words = ["what", "does", "this", "line", "do", "?"]  # This made a list

# I think it will print the first word in the list
for word in some_words:
    print(word)  # It prints the list with the words on different lines

# I think it will print the list with the words on different lines
for x in some_words:
    print(x)  # It printed the list with the words on different lines

# I think it will print the list
print(some_words)  # It printed the list

# I think that it will print "some_words contains more than 3 words"
if len(some_words) > 3:
    print(
        "some_words contains more than 3 words"
    )  # It printed as there is more than 3 words

# I think it will print the system attributes
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())  # It printed the system attributes


usefulFunction()
