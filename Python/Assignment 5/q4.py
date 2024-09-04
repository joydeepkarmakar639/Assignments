# Create the set of IT companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# I. Find the length of the set it_companies
length_of_set = len(it_companies)
print("Length of it_companies:", length_of_set)

# II. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("Set after adding 'Twitter':", it_companies)

# III. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Netflix', 'Tesla', 'Adobe'])
print("Set after adding multiple companies:", it_companies)

# IV. Remove one of the companies from the set it_companies
it_companies.remove('Facebook')  # Removing 'Facebook' as an example
print("Set after removing 'Facebook':", it_companies)

# V. Difference between remove and discard
# - remove: Removes the specified element from the set. Raises a KeyError if the element does not exist.
# - discard: Removes the specified element from the set. Does not raise an error if the element does not exist.

# Example:
it_companies.discard('NonExistentCompany')  # No error
# it_companies.remove('NonExistentCompany')  # This would raise a KeyError
