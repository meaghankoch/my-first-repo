# total_comprehension.py
#
my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)
#
print("--------------")
print("TOTAL COMPREHENSION...")


print (len(my_numbers))
print(min(my_numbers))
my_numbers.reverse()
print(my_numbers)


def  enlarge (my_numbers):
    return (100 * my_numbers)

new_numbers = map(enlarge, my_numbers)
print(list(new_numbers))

def greater_than_three(my_numbers):
    return my_numbers > 3
print(list(filter(greater_than_three, my_numbers))) 

def greater_than_eight(my_numbers):
    return my_numbers > 8
print(list(filter(greater_than_eight,my_numbers)))


def  enlarge (my_numbers):
    return (100 * my_numbers)

new_numbers = map(enlarge, my_numbers)

def greater_than_three(new_numbers):
    return new_numbers > 300

print(list(filter(greater_than_three,new_numbers)))



