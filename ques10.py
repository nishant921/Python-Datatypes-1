# Problem 10: Add Space between Potential Words.
# Example:

# Input:

# ['campusxIs', 'bestFor', 'dataScientist']   
# Output:

# ['campusx Is', 'best For', 'data Scientist']


l= ['campusxIs', 'bestFor', 'dataScientist']   
result=[''.join((" "+ch)if ch.isupper() else ch for ch in word)for word in l]
print(result)