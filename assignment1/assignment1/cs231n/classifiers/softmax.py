from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.

    loss = 0.0
    dW = np.zeros(W.shape)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num_train = X.shape[0]
    num_dim = W.shape[0]
    num_class = W.shape[1]
    for i in range(num_train):
        scores = np.dot(X[i], W)
        l_i = 0
        makhraj = np.exp(scores)
        makhraj_sum = np.sum(makhraj)
        l_i = -np.log(np.exp(scores[y[i]]) / makhraj_sum)
        loss += l_i
        for j in range(num_class):
            dW[:, j] += X[i, : ] * (makhraj[j] / makhraj_sum)
        dW[:, y[i]] -= X[i,  : ]
        
    loss /= num_train
    dW /= num_train
    loss += reg * np.sum(W * W)
    dW += 2 * reg * W
    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num_train = X.shape[0]
    num_dim = W.shape[0]
    num_class = W.shape[1]
    score = np.dot(X, W)
    score2 = np.exp(score)
    score_sum = np.log(np.sum(score2, 1))
    true_score = -1 * score[np.arange(num_train), y]
    loss = np.sum(true_score + score_sum)
    loss /= num_train
    loss += reg * np.sum(W * W)
    score2_sum = 1 / np.sum(score2, 1)
    temp = score2 * score2_sum[:, np.newaxis]
    temp[np.arange(num_train), y] -=1
    dW = np.dot(X.T, temp)
    dW /= num_train
    dW += 2 * reg * W
    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
