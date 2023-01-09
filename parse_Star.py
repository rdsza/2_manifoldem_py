import pystar

"""
This code parses the Relion star file data.star, and access the data 
stored in the file using the pystar library. The data is stored in data blocks, 
with each data block containing a set of columns and rows. You can
access the columns and rows using the columns attribute and the for loop, respectively.
"""

# Parse the star file
star = pystar.parse("data.star")

# Access the data blocks
data_blocks = star.data_blocks

# Access the first data block
data_block = data_blocks[0]

# Access the columns in the data block
columns = data_block.columns

# Access the values in a particular column
values = data_block.columns['rlnImageName']

# Iterate over the rows in the data block
for row in data_block:
    image_name = row['rlnImageName']
    pixel_size = row['rlnPixelSize']
    ...
