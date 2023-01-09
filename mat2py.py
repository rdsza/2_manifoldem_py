import scipy.io
import numpy as np

def mat_to_npz(mat_file, npz_file):
    """
    Load a .mat file using the `scipy.io.loadmat` function, convert it
    to a dictionary, and then save the dictionary to a .npz file using
    the `numpy.savez` function.
    
    Usage :
    mat_to_npz('file.mat', 'file.npz')

    """
    mat = scipy.io.loadmat(mat_file)

    # Convert the loaded .mat file to a dictionary
    data = {k:v for k, v in mat.items() if k[0] != '_'}

    # Save the dictionary to a .npz file
    np.savez(npz_file, **data)


def mat_to_npz_var(mat_file, npz_file, *variables):
    """
    You can also specify the variables you want to include in the .npz file 
    by passing them as keyword arguments to the numpy.savez function,
    like this:
    """
    # Load the .mat file
    mat = scipy.io.loadmat(mat_file)

    # Convert the loaded .mat file to a dictionary
    data = {k:v for k, v in mat.items() if k[0] != '_'}

    # Save the specified variables to a .npz file
    np.savez(npz_file, *[(var, data[var]) for var in variables])
