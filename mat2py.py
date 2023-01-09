

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


