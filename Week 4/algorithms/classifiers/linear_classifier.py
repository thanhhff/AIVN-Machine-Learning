import numpy as np
from algorithms.classifiers.loss_grad_logistic import *
from algorithms.classifiers.loss_grad_softmax import *
from algorithms.classifiers.loss_grad_svm import *

class LinearClassifier:

    def __init__(self):
        self.W = None # set up the weight matrix 

    def train(self, X, y, method='sgd', batch_size=200, learning_rate=1e-4,
              reg = 1e3, num_iters=1000, verbose=False, vectorized=True):
        """
        Train linear classifer using batch gradient descent or stochastic gradient descent

        Parameters
        ----------
        X: (D x N) array of training data, each column is a training sample with D-dimension.
        y: (N, ) 1-dimension array of target data with length N.
        method: (string) determine whether using 'bgd' or 'sgd'.
        batch_size: (integer) number of training examples to use at each step.
        learning_rate: (float) learning rate for optimization.
        reg: (float) regularization strength for optimization.
        num_iters: (integer) number of steps to take when optimization.
        verbose: (boolean) if True, print out the progress (loss) when optimization.

        Returns
        -------
        losses_history: (list) of losses at each training iteration
        """

        dim, num_train = X.shape
        num_classes = np.max(y) + 1 # assume y takes values 0...K-1 where K is number of classes

        if self.W is None:
            # initialize the weights with small values
            if num_classes == 2: # just need weights for one class
                self.W = np.random.randn(1, dim) * 0.001
            else: # weigths for each class
                self.W = np.random.randn(num_classes, dim) * 0.001

        losses_history = []

        for i in range(num_iters):
            if method == 'bgd':
                loss, grad = self.loss_grad(X, y, reg, vectorized)
            else:
                # randomly choose a min-batch of samples
                idxs = np.random.choice(num_train, batch_size, replace=False)
                loss, grad = self.loss_grad(X[:, idxs], y[idxs], reg, vectorized) # grad => [K x D]
            losses_history.append(loss)

            # update weights
            self.W -= learning_rate * grad # [K x D]
            # print self.W
            # print 'dsfad', grad.shape
            if verbose and (i % 100 == 0):
                print('iteration %d/%d: loss %f' % (i, num_iters, loss))

        return losses_history

    def predict(self, X):
        """
        Predict value of y using trained weights

        Parameters
        ----------
        X: (D x N) array of data, each column is a sample with D-dimension.

        Returns
        -------
        pred_ys: (N, ) 1-dimension array of y for N sampels
        h_x_mat: Normalized scores
        """
        pred_ys = np.zeros(X.shape[1])
        f_x_mat = self.W.dot(X)
        if self.__class__.__name__ == 'Logistic':
            pred_ys = f_x_mat.squeeze() >=0
        else: # multiclassification
            pred_ys = np.argmax(f_x_mat, axis=0)
        # normalized score
        h_x_mat = 1.0 / (1.0 + np.exp(-f_x_mat)) # [1, N]
        h_x_mat = h_x_mat.squeeze()
        return pred_ys, h_x_mat

    def loss_grad(self, X, y, reg, vectorized=True):
        """
        Compute the loss and gradients.

        Parameters
        ----------
        The same as self.train()

        Returns
        -------
        a tuple of two items (loss, grad)
        loss: (float)
        grad: (array) with respect to self.W
        """
        pass


# Subclasses of linear classifier
class Logistic(LinearClassifier):
    """A subclass for binary classification using logistic function"""
    def loss_grad(self, X, y, reg, vectorized=True):
        if vectorized:
            return loss_grad_logistic_vectorized(self.W, X, y, reg)
        else:
            return loss_grad_logistic_naive(self.W, X, y, reg)


class Softmax(LinearClassifier):
    """A subclass for multi-classicication using Softmax function"""
    def loss_grad(self, X, y, reg, vectorized=True):
        if vectorized:
            return loss_grad_softmax_vectorized(self.W, X, y, reg)
        else:
            return loss_grad_softmax_naive(self.W, X, y, reg)


class SVM(LinearClassifier):
    """A subclass for multi-classicication using SVM function"""
    def loss_grad(self, X, y, reg, vectorized=True):
        return loss_grad_svm_vectorized(self.W, X, y, reg)


