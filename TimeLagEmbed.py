"""
This code uses a sliding window to perform time-lagged embedding on the time series data, 
with a specified lag time of lag steps. The resulting embedded data is then reduced to two 
dimensions using multidimensional scaling (MDS) from scikit-learn's manifold module.
"""
import numpy as np
from sklearn.manifold import MDS

# Load the time series data
X = np.load("timeseries.npy")

# Set the lag time for the embedding
lag = 10

# Perform time-lagged embedding
X_embedded = []
for i in range(len(X) - lag):
    x = X[i:i+lag]
    X_embedded.append(x)
X_embedded = np.array(X_embedded)

# Perform dimensionality reduction on the embedded data
mds = MDS(n_components=2)
X_reduced = mds.fit_transform(X_embedded)

# Do something with the reduced data (e.g., visualize, cluster, etc.)
