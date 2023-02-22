"""pyupgrade --py36-plus ./notebooks/pyupgrade.py"""

# In python3.8+, comparison to literals becomes a SyntaxWarning as the success of those comparisons
# is implementation specific (due to common object caching).
NUMBER = 1
# print(NUMBER is 5)
print(NUMBER is 5)


# f-strings
# print("The number is {}".format(NUMBER))
print("The number is {}".format(NUMBER))
