def purify(numbers_list):
    even_numbers = list()
    for n in numbers_list:
        if n % 2 == 0:
           even_numbers.append(n)
    return (even_numbers)