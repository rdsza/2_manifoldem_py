"""
This code computes the diffusion maps representation of the input data X, 
using the affinity matrix A constructed from the pairwise distances between the samples. T
he resulting diffusion maps representation is stored in the X_diffmap variable, which is a
matrix with k columns, where k is the number of dimensions specified.
"""

import numpy as np
from sklearn.manifold import SpectralEmbedding

# Load the data
X = np.load('data.npy')

# Compute the pairwise distances between all samples
D = squareform(pdist(X))

# Construct the affinity matrix
eps = 0.1 # specify the width of the Gaussian kernel
A = np.exp(-D**2 / eps**2)

# Normalize the affinity matrix
D = np.diag(A.sum(axis=1))
L = D - A

# Compute the eigenvectors and eigenvalues of the Laplacian matrix
eigenvals, eigenvecs = np.linalg.eigh(L)

# Select the top k eigenvectors
k = 2 # number of dimensions
X_diffmap = eigenvecs[:,:k]
