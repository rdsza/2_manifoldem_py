"""
This code performs spectral embedding on the combined data clusters to map them to a latent space.
The resulting latent space is then split back into the original clusters using indexing.
Finally, the clusters are aligned in the latent space by shifting their means to match each other.

"""

import numpy as np
from sklearn.manifold import SpectralEmbedding

# Load the two data clusters
X1 = np.load("cluster1.npy")
X2 = np.load("cluster2.npy")

# Concatenate the two data clusters
X = np.concatenate((X1, X2), axis=0)

# Perform spectral embedding on the combined data
se = SpectralEmbedding(n_components=2)
X_embedded = se.fit_transform(X)

# Split the embedded data back into the original clusters
X1_embedded = X_embedded[:len(X1)]
X2_embedded = X_embedded[len(X1):]

# Align the two clusters in latent space
X1_mean = np.mean(X1_embedded, axis=0)
X2_mean = np.mean(X2_embedded, axis=0)
X1_aligned = X1_embedded - X1_mean + X2_mean
X2_aligned = X2_embedded - X2_mean + X1_mean
