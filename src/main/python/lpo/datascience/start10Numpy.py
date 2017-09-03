# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# Calculate bmi (ou IMC)
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

# For a boolean response
print(bmi > 24)

# Print only those observations above 23
print(bmi[bmi > 24])


# ***** exercise
# First, convert the list of weights from a list to a Numpy array.
# Then, convert all of the weights from kilograms to pounds.
# Use the scalar conversion of 2.2 lbs per kilogram to make your conversion.
# Lastly, print the resulting array of weights in pounds.

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight = np.array(weight_kg)


# Create np_weight_lbs from np_weight_kg
np_pounds = np_weight * 2.2

# Print out np_weight_lbs
print(np_pounds)