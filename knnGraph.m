
%  This code will compute the k nearest neighbor graph for the input data X, 
%   using the number of nearest neighbors k specified. The resulting graph is
%   represented by the adjacency matrix A.
%


% Load the data
data = load('data.mat');
X = data.X; % assume X is a matrix of size NxD, where N is the number of samples and D is the number of features

% Choose the number of nearest neighbors
k = 10;

% Compute the pairwise distances between all samples
D = squareform(pdist(X));

% Sort the distances in ascending order
[sortedD, sortedIdx] = sort(D, 2);

% Keep only the k nearest neighbors for each sample
kNNIdx = sortedIdx(:, 2:k+1);

% Create the adjacency matrix of the kNN graph
A = zeros(size(X,1));
for i = 1:size(X,1)
    A(i, kNNIdx(i,:)) = 1;
end
A = A + A'; % make the graph undirected
