"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.00
numChars = int(input("Enter number of characters: "))
woodType = input("Enter wood type (pine or oak): ")
color = input("Enter color of characters (black, white, or gold): ")

# Charge for this sign.
charge += 35.00

# Number of characters.

if numChars > 5:
  charge += (numChars - 5) * 4
  
# Color of characters.

if color == "gold":
  charge += 15.00
elif color == "black" or color == "white":
  charge += 0

# Type of wood.

if woodType == "oak":
  charge += 20
elif woodType == "pine":
  charge += 0

# Write assignment and if statements here as appropriate.

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
