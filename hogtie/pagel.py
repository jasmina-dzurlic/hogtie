#! usr/bin/env python

import numpy as np
import pandas as pd
import toytree
from scipy.optimize import minimize
from scipy.linalg import expm

def assign_tip_like_values(tree, data):
    """
    Assigns likelihood values to tree tips
    """
    values = [{0:-(i-1),1:i} for i in data]
    keys = list(range(0, len(data), 1))
    valuesdict = dict(zip(keys,values))
    tree = tree.set_node_values(feature = "likelihood", values = valuesdict)

def cond_like(likeleft0, likeleft1, likeright0, likeright1, tL, tR, alpha, beta):
	"""
	Calculates conditional likelihood of character states at each node
	"""
    Q = np.array([[-alpha, alpha], [beta, -beta]])
    probleft = expm(Q*tL)
    probright = expm(Q*tR)
 
    #ancestor is 0
    left0 = probleft[0, 0] * likeleft0 + probleft[0, 1] * likeleft1
    right0 = probright[0, 0] * likeright0 + probright[0, 1] * likeright1
    like_zero = left0*right0
 
    #ancestor is 1
    left1 = probleft[1, 0] * likeleft0 + probleft[1, 1] * likeleft1
    right1 = probright[1, 0] * likeright0 + probright[1, 1] * likeright1
    like_one = left1*right1
 
    return {0: like_zero, 1: like_one}

def pruningalg(tree, alpha, beta):
	"""
	Runs Felsenstein's pruning algorithm on an input tree, given instantaneous transition
	rates alpha and beta. Assigns likelihood scores for characters states at each node.
	Specifically for binary state model. 
	"""
    for node in tree.treenode.traverse("postorder"):
        if len(node.children) == 2:
            child1 = node.children[0]
            child2 = node.children[1]
            likedict = cond_like(likeright0 = child1.likelihood[0],
                                 likeright1 = child1.likelihood[1],
                                 likeleft0 = child2.likelihood[0],
                                 likeleft1 = child2.likelihood[1],
                                 tR = child1.dist,
                                 tL = child2.dist,
                                 alpha = alpha,
                                 beta = beta)
            node.likelihood = likedict

def node_like(tree):
    """
    Get negetive likelihood value at each node
    """
    tree.set_node_values('neglike')
    for node in tree.treenode.traverse('postorder'):
        like = node.likelihood[0]*0.5 + node.likelihood[1]*0.5
        node.neglike = -like
    return tree

def model_fit(tree): #still fixing bugs
    """
    Find the maximum likelihood estimate of the two
    rate model parameters at each node given the data.
    """
    tree.set_node_values('alpha')
    tree.set_node_values('beta')
    for node in tree.treenode.traverse('postorder'):
        estimate = minimize(
            fun=node_like,
            x0=np.array([1., 1.]),
            method='L-BFGS-B',
            bounds=((0, 10), (0, 10))
            )
        result = {
            'alpha': round(estimate.x[0], 3),
            'beta': round(estimate.x[1], 3), 
            'convergence': estimate.success,
            }
        node.alpha = result['alpha']
        node.beta = result['beta']
    return tree
