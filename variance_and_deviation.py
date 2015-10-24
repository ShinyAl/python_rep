""""The variance allows us to see how widespread the grades 
were from the average.
the grades varied against the average. This is called computing the variance.

A very large variance means that the students' grades were all over the place, 
while a small variance (relatively close to the average) 
means that the majority of students did fairly well.

The standard deviation is the square root of the variance. You can calculate 
the square root by raising the number to the one-half power."""

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance = variance + (average - score) ** 2
        total_variance = variance / len(scores)
    return total_variance
#print grades_variance(grades)

def grades_std_deviation(variance):
    return variance ** 0.5
variance = grades_variance(grades)
print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)


