def linear_search(arr, item):
    """ Searches for an item in a given list and returns
        True or False depending if the item is found
        args:
            arr: list,
            item: any type """
    for i in arr:
        if i == item:
            return True
    return False
