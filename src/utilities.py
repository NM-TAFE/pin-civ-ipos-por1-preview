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