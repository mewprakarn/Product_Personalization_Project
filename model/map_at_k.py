import pandas as pd
import numpy as np

# https://www.kaggle.com/c/h-and-m-personalized-fashion-recommendations/discussion/306007
# https://github.com/benhamner/Metrics/blob/master/Python/ml_metrics/average_precision.py

def apk(actual, predicted, k=10):
    """
    Computes the average precision at k.
    This function computes the average prescision at k between two lists of
    items.
    Parameters
    ----------
    actual : list
             A list of elements that are to be predicted (order doesn't matter)
    predicted : list
                A list of predicted elements (order does matter)
    k : int, optional
        The maximum number of predicted elements
    Returns
    -------
    score : double
            The average precision at k over the input lists
    """
    
    if len(predicted)>k:
        predicted = predicted[:k]

    score = 0.0
    num_hits = 0.0

    for i,p in enumerate(predicted):
#         print('items 1: ')
        if p in actual and p not in predicted[:i]:
            num_hits += 1.0
            score += num_hits / (i+1.0)
#             print('num_hits: ',num_hits)
#             print('score: ',score)
#             print('final score:', score / min(len(actual), k))
#             print('='*50)
    # remove this case in advance
#     if not actual:
#         return 0.0
    try:
        return score / min(len(actual), k)
    except:
        return 0


def mapk(actual, predicted, k=10):
    """
    Computes the mean average precision at k.
    This function computes the mean average prescision at k between two lists
    of lists of items.
    Parameters
    ----------
    actual : list
             A list of lists of elements that are to be predicted 
             (order doesn't matter in the lists)
    predicted : list
                A list of lists of predicted elements
                (order matters in the lists)
    k : int, optional
        The maximum number of predicted elements
    Returns
    -------
    score : double
            The mean average precision at k over the input lists
    """
#     print([apk(a,p,k) for a,p in zip(actual, predicted)]) 
    return np.mean([apk(a,p,k) for a,p in zip(actual, predicted)]) 