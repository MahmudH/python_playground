age = input("Enter your age")
# print "You have been living for " + str(int(age) * 365 * 24 * 60 * 60) + " seconds. This corresponds to " + str(age) + " years"
print("You lived for {} seconds. This corresponds to {} years.".format(int(age) * 365 * 24 * 60 * 60, age))