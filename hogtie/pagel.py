#! usr/bin/env python

import numpy as np
import pandas as pd
import toytree
from scipy.optimize import minimize
from scipy.linalg import expm

def datatodict(data):
	"""
	Parses data into format that can be used by the cond_like and
	pruningalg functions
	"""
    values = [{0:-(i-1),1:i} for i in data]
    keys = list(range(0, len(mydata), 1))
    valuesdict = dict(zip(keys,values))
    return valuesdict

def assignnodevalues(tree, values):
	"""
	Assigns likelihood values to tree tips
	"""
    likelihood = datatodict(data = data)
    tree.set_node_values(feature = "likelihood", values = likelihood)
	pass

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
