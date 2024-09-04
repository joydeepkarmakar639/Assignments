# List of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# I. Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}")
print(f"Max age: {max_age}")

# II. Add the min age and the max age again to the list
ages.extend([min_age, max_age])
print(f"Ages after adding min and max again: {ages}")

# III. Find the median age
ages.sort()
length = len(ages)
if length % 2 == 0:
    median_age = (ages[length // 2 - 1] + ages[length // 2]) / 2
else:
    median_age = ages[length // 2]
print(f"Median age: {median_age}")

# IV. Find the average age
average_age = sum(ages) / len(ages)
print(f"Average age: {average_age:.2f}")

# V. Find the range of the ages
age_range = max_age - min_age
print(f"Range of ages: {age_range}")

# VI. Compare the value of (min - average) and (max - average), using abs() method
min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)
print(f"abs(min - average): {min_avg_diff:.2f}")
print(f"abs(max - average): {max_avg_diff:.2f}")
