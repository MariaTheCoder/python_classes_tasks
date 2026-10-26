# Application which distributes a bill from a restaurant between a group of friends.
# We assume that there are 3 friends.

# -------------------------------------------------------------------

# We assume that there are 3 friends present
# friends = 3

# Make the user input a total bill cost
# total_bill_excl_tips = float(input("How much was the restaurant bill in total, tips exclusive? "))

# total_bill_incl_tips = total_bill_excl_tips * 1.15

# Prints fordi det er rart at se
# print(f"Total bill excl tips = {total_bill_excl_tips}")
# print(f"Total bill incl tips = {total_bill_incl_tips}")

# Calculate how much each friend has to pay, tips included
# print(f"\nBill per person incl. tips: {round(total_bill_incl_tips/friends,2)}")

# -------------------------------------------------------------------

# Ask the user for the names of each friend
# friend1_name = input("Type your first friend's name: ")
# friend2_name = input("Type your second friend's name: ")
# friend3_name = input("Type your third friend's name: ")

# Type in the total bill, tips excluded
bill_excl_tips = float(input("Total bill excl. tips: "))

# Let the user tell us how many percent they decide to tip
tip = float(input("Total tip in percentage: "))

# Calculate tip amount
tip_amount = bill_excl_tips / 100 * tip

# Calculate how much the total bill is
bill_incl_tips = bill_excl_tips + tip_amount

print(f"Total bill incl. tips: {bill_incl_tips}")
print(f"Each of the three friends needs to pay {round(bill_incl_tips/3,2)} DKK.")