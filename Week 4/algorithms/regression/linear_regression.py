import numpy as np

class LinearRegression:

    def __init__(self):
        self.W = None # set the weight vector

    def train(self, X, y, method='bgd', learning_rate=1e-2, num_iters=100, verbose=False):
        """
        Train linear regression using batch gradient descent or stochastic gradient descent

        Inputs
        ----------
        X: (D x N) array of training data, each column is a training sample with D-dimension.
        y: (N, ) 1-dimension array of target data with length N. 
        method: (string) determine wheter use 'bgd' or 'sgd'
        learning_rate: (float) learning rate for optimization
        num_iters: (integer) number of steps to take when optimization
        verbose: (boolean) if True, print out the progress when optimization

        Returns
        -------
        losses_history: (list) of losses at each training iteration
        """
        dim, num_train = X.shape

        if self.W is None:
            # initilize weights with small values
            self.W = np.random.randn(1, dim) * 0.001 # [1, D]

        losses_history = []

        for i in xrange(num_iters):

            if method == 'sgd':
                # randomly choose a sample
                idx = np.random.choice(num_train)
                
                loss, grad = self.loss_grad(X[:, idx, np.newaxis], y[idx, np.newaxis])

            else:
                loss, grad = self.loss_grad(X, y)

            losses_history.append(loss)

            # Update weights using matrix computing (vectorized)
            self.W -= learning_rate * grad

            if verbose and i % (num_iters / 10) == 0:
                print 'iteration %d / %d : loss %f' %(i, num_iters, loss)
        return losses_history


    def predict(self, X):
        """
        Predict value of y using trained weights

        Inputs
        ----------
        X: (D x N) array of data, each column is a sample with D-dimension.

        Returns
        -------
        pred_ys: (N, ) 1-dimension array of y for N sampels
        """
        pred_ys = self.W.dot(X)

        return pred_ys


    def loss_grad(self, X, y, vectorized=True):
        """
        Compute the loss and gradients

        Inputs
        ------
        The same as self.train function

        Returns
        -------
        a tuple of two items (loss, grad)
        loss: (float)
        grad: (array) with respect to self.W 
        """
        if vectorized:
            return linear_loss_grad(self.W, X, y)
        else:
            return linear_loss_grad_naive(self.W, X, y)


def linear_loss_grad(W, X, y):
    """
    Compute the loss and gradients with weights, vectorized version

    Parameters and Returns are the same as LinearRegression.loss_grad, except including W as parameter
    """
    # vectorized implementation 
    num_train = X.shape[1]
    f_mat = W.dot(X) # [1, D] * [D, N]
    diff = f_mat - y # [1, N] - [1, N]
    loss = 1.0 / (2 * num_train) * np.sum(diff * diff) # [1, N] * [N, 1] 
    grad = 1.0 / num_train * diff.dot(X.T) # [1, N] * [N, D]

    return (loss, grad)

def linear_loss_grad_naive(W, X, y):
    """
    Compute the loss and gradients with weights, for loop version
    """
    num_train = X.shape[1]

    loss = 0
    grad = np.zeros_like(W) # [1, D]

    for i in xrange(num_train):
        sample_X = X[:, i] # a vector
        f = 0
        for j in xrange(W.shape[1]):
            f += sample_X[j] * W[0, j]

        diff = f - y[i]
        loss += diff ** 2

        for j in xrange(W.shape[1]):
            grad[0, j] += diff * sample_X[j]
            
    loss = 1.0 / (2 * num_train) * loss

    grad = 1.0 / (num_train) * grad

    return (loss, grad)








