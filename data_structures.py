tuple_grade = (77, 79, 100)

tuple_grade += (200,)

print(tuple_grade)

# Set operations

lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

print(lottery_numbers.intersection(winning_numbers))

print(lottery_numbers.union(winning_numbers))
