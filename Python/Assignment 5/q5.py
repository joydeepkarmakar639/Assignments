# Define the sets A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# I. Join A and B (Union of A and B)
joined_AB = A.union(B)
print("Joined A and B (A ∪ B):", joined_AB)

# II. Find A intersection B
intersection_AB = A.intersection(B)
print("Intersection of A and B (A ∩ B):", intersection_AB)

# III. Is A subset of B
is_A_subset_B = A.issubset(B)
print("Is A a subset of B?:", is_A_subset_B)

# IV. Are A and B disjoint sets
are_A_B_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?:", are_A_B_disjoint)

# V. Join A with B and B with A (Union is commutative, so it's the same)
joined_A_with_B = A.union(B)
joined_B_with_A = B.union(A)
print("Join A with B:", joined_A_with_B)
print("Join B with A:", joined_B_with_A)

# VI. What is the symmetric difference between A and B
symmetric_difference_AB = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_difference_AB)

# VII. Delete the sets completely
del A
del B

# Attempting to print A or B will raise an error because they are deleted
try:
    print(A)
    print(B)
except NameError:
    print("Set A & B have been deleted.")
