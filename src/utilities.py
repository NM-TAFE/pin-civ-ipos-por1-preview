"""
Utility functions for the Tic-Tac-Toe game.
Author: Emily Boegheim
"""


def all_items_in_collection_equal(collection):
    """
    Check whether all items in a given collection (e.g. a list) are equal to
    one another.
    :param collection: The iterable to check for equality.
    :returns: True if all items in the collection are equal, False if they are
        not or if an empty collection is passed in.
    """
    if len(collection) < 1:
        return False
    else:
        sample = collection[0]
        for item in collection[1:]:
            if item != sample:
                return False
        return True


def get_int_from_input(prompt="Please enter an integer: ",
                       error="Please enter a valid integer."):
    """
    Prompts the user to enter an integer using the console and parses the
    input. If the user's input cannot be parsed as an integer, prints an error
    and continues the prompt the user for input. Once the user enters a valid
    integer, returns the integer.
    :param prompt: Text to prompt the user for input.
    :param error: Error message to print if the user's input cannot be parsed
        as an integer.
    :returns: The user's input as an integer.
    """
    while True:
        user_input = input(prompt)
        try:
            user_int = int(user_input)
            return user_int
        except ValueError:
            print(error)
