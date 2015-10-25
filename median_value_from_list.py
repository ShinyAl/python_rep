lists = [12, 34, 56, 70, 80]

def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        first_middle_index = len(numbers) // 2
        second_middle_index = first_middle_index - 1
        median = (numbers[first_middle_index] + numbers[second_middle_index]) / 2
        return median
    else:
        index = len(numbers) // 2
        median = numbers[index]
        return median

print (median(lists))