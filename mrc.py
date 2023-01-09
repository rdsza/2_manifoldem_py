"""
This code uses the mrcfile library to open the .mrc file and 
extract the data from it. The data is stored in a NumPy array, 
which can then be used for further processing or analysis.
"""
import numpy as np
import mrcfile

# Open the .mrc file
with mrcfile.open("data.mrc") as mrc:
    # Extract the data from the file
    data = mrc.data
