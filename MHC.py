# This file contains functions that will be made and imported for multiple hypothesis correction

def bonferroni(p_val_array, alpha):
    num_tests = len(p_val_array)
    bonferroni_alpha = alpha / num_tests
    return bonferroni_alpha


def fdr(p_val_array, alpha):
    """
    Put your code here, remember that p_val_array is not sorted
    """
    fdr_alpha = None
    return fdr_alpha