def count(sequence, item):
    found = 0
    for thing in sequence:
        if item == thing:
            found += 1
    return found