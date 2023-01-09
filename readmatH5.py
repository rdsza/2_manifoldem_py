import h5py

def read_mat(mat_file):
    with h5py.File(mat_file, 'r') as f:
        # Get the list of keys in the file
        keys = list(f.keys())

        # Initialize a dictionary to store the data
        data = {}

        # Iterate through the keys and store the data in the dictionary
        for key in keys:
            data[key] = f[key][()]

    return data