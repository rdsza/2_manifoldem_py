import numpy as np

def L2_distance(dataset1, dataset2):
  """Calculates the L2 distance between two datasets.
  
  Parameters
  ----------
  dataset1 : array-like
    The first dataset, with shape (N,M).
  dataset2 : array-like
    The second dataset, with shape (N,M).
    
  
  Returns
  -------
  distance : float
    The L2 distance between thw two datasets.
  """
  
 # Convert the datasets to NumPy arrays
 dataset1 = np.array(dataset1)
 dataset2 = np.array(dataset2)
 
 # Calculate the distance
 distance = np.sqrt(np.sum((dataset1-dataset2)**2))
 
 return distance
 
 
 # Calculate the L2 distance between two datasets
 dataset1 = [[1, 2, 3], [4, 5, 6]]
 dataset2 = [[7, 8, 9], [10, 11, 12]]
 distance = L2_distance(dataset1, dataset2)
 
 print(distance)
