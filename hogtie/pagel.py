#! usr/bin/env python

import numpy as np
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
    return tree

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


def node_like(x0, likeleft0, likeleft1, likeright0, likeright1, tL, tR, anca):
  
    condlik = cond_like(likeleft0, likeleft1, likeright0, likeright1, tL, tR, x0[0], x0[1])
  
    # get full likelihood
    lik = (1 - anca) * condlik[0] + (anca) * condlik[1]
  
    # I don't understand this part
    if anca in [0., 1.]:
        lik /= 2
 
    return -lik #np.log(lik)

def model_fit(likeleft0, likeleft1, likeright0, likeright1, tL, tR, anca):
    """
    Find the maximum likelihood estimate of the two
    rate model parameters at each node given the data.
    """
    args = (likeleft0, likeleft1, likeright0, likeright1, tL, tR, anca)
   
    # ML estimate
    estimate = minimize(
       fun=node_like, 
        x0=np.array([1., 1.]),
        args=args,
        method='L-BFGS-B',
        bounds=((0, 10), (0, 10))
    )
   
    score = -1 * node_like(estimate.x, *args)
    result = {
        "alpha": round(estimate.x[0], 3),
        "beta": round(estimate.x[1], 3), 
        "lik": round(score, 3),
        "convergence": estimate.success,
    }
    return result

def fit_model_at_nodes(tree):
    tree = tree.set_node_values('alpha')
    tree = tree.set_node_values('beta')
    for node in tree.treenode.traverse("postorder"):
        if len(node.children) == 2:
            child1 = node.children[0]
            child2 = node.children[1]
            model = model_fit(likeright0 = child1.likelihood[0],
                              likeright1 = child1.likelihood[1],
                              likeleft0 = child2.likelihood[0],
                              likeleft1 = child2.likelihood[1],
                              tR = child1.dist,
                              tL = child2.dist,
                              anca = 0.5)
            node.alpha = model['alpha']
            node.beta = model['beta']
    return tree
def pruning_alg(tree):
    """
    Runs Felsenstein's pruning algorithm on an input tree, given instantaneous transition
    rates alpha and beta. Assigns likelihood scores for characters states at each node.
    Specifically for binary state model. 
    """
    tree = fit_model_at_nodes(tree)
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
                                 alpha = float(node.alpha),
                                 beta = float(node.beta)
                                 )
            node.likelihood = likedict
            return tree


if __name__ == "__main__":
    tree1 = toytree.rtree.unittree(ntips=10)
    data1 = [0,1,1,0,1,1,0,0,0,1]
    tree1 = assign_tip_like_values(tree1, data1)
    tree1 = pruning_alg(tree1)