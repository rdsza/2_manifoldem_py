import numpy as np
from sklearn.manifold import MDS

def diffusion_map(images, n_components=2):
    """
    Performs diffusion maps on a set of images.
    
    Parameters
    ----------
    images : array-like, shape (n_samples, n_features)
        The set of images to be analyzed. Each row represents a single image.
    n_components : int, optional
        The number of dimensions to use in the diffusion map. The default is 2.
        
    Returns
    -------
    embedding : array-like, shape (n_samples, n_components)
        The low-dimensional embedding of the images in the diffusion map.
    """
    # Compute the pairwise distances between images
    distances = np.sqrt(np.sum((images[:, np.newaxis] - images[np.newaxis, :]) ** 2, axis=-1))
    
    # Compute the diffusion map
    mds = MDS(n_components=n_components, dissimilarity='precomputed')
    embedding = mds.fit_transform(distances)
    
    return embedding
