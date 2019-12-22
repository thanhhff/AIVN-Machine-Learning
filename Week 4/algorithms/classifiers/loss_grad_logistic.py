# file: algorithms/classifiers/loss_grad_logistic.py
import numpy as np

def loss_grad_logistic_naive(W, X, y, reg):
    """
    Compute the loss and gradients using logistic function 
    with loop, which is slow.

    Parameters
    ----------
    W: (1, D) array of weights, D is the dimension of one sample.
    X: (D, N) array of training data, each column is a training sample with D-dimension.
    y: (N, ) 1-dimension array of target data with length N.
    reg: (float) regularization strength for optimization.

    Returns
    -------
    a tuple of two items (loss, grad)
    loss: (float)
    grad: (array) with respect to self.W
    """
    dim, num_train = X.shape
    loss = 0
    grad = np.zeros_like(W) # [1, D]
    for i in xrange(num_train):
        sample_x = X[:, i]
        f_x = 0
        for idx in xrange(sample_x.shape[0]):
            f_x += W[0, idx] * sample_x[idx]
        h_x = 1.0 / (1 + np.exp(-f_x))
        loss += y[i] * np.log(h_x) + (1 - y[i]) * np.log(1 - h_x)

        grad += (h_x - y[i]) * sample_x # [D, ]
    loss /= -num_train
    loss += 0.5 * reg * np.sum(W * W) # add regularization

    grad /= num_train
    grad += reg * W # add regularization
    return loss, grad

def loss_grad_logistic_vectorized(W, X, y, reg):
    """Compute the loss and gradients with weights, vectorized version"""
    dim, num_train = X.shape
    loss = 0
    grad = np.zeros_like(W) # [1, D]
    # print W
    f_x_mat = W.dot(X) # [1, D] * [D, N]
    h_x_mat = 1.0 / (1.0 + np.exp(-f_x_mat)) # [1, N]
    loss = np.sum(y * np.log(h_x_mat) + (1 - y) * np.log(1 - h_x_mat))
    loss = -1.0 / num_train * loss + 0.5 * reg * np.sum(W * W)
    grad = (h_x_mat - y).dot(X.T) # [1, D]
    grad = 1.0 / num_train * grad + reg * W
    
    return loss, grad





