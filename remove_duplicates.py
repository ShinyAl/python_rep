def remove_duplicates(items):
    without_duplicate = list()
    for item in items:
        if item not in without_duplicate:
            without_duplicate.append(item)
    return without_duplicate