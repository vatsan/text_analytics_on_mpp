""" 
   Simple skipgram generator using itertools
   Srivatsan Ramanujam <vatsan.cs@utexas.edu>, Nov 2015
"""
from itertools import combinations
import ast

def is_valid_k_skip(lst, k):
    """
        Validate if a given n-gram list (of token indices) contains valid k-skips.
        For instance, a 2-skip bigram, includes 0-skip bigrams, 1-skip bigrams 
        and 2-skip bigrams.
    """
    idx_diff = [(next_idx - current_idx) for current_idx, next_idx in zip(lst, lst[1:])]
    valid_skips = set(range(k+2))
    return len(set(idx_diff))==1 and (set(idx_diff).pop() in valid_skips)

def generate_k_skip_n_gram(lst, k, n):
    """
        Return all k-skip, n-grams as defined in 
        http://homepages.inf.ed.ac.uk/ballison/pdf/lrec_skipgrams.pdf
        ex: "Insurgents killed in ongoing fighting"
        Bi-grams = {insurgents killed, killed in, in ongoing,
        ongoing fighting}.
        2-skip-bi-grams = {insurgents killed, insurgents in,
        insurgents ongoing, killed in, killed ongoing, killed
        fighting, in ongoing, in fighting, ongoing fighting}
        Tri-grams = {insurgents killed in, killed in ongoing, in
        ongoing fighting}.
        2-skip-tri-grams = {insurgents killed in, insurgents killed
        ongoing, insurgents killed fighting, insurgents in ongoing,
        insurgents in fighting, insurgents ongoing fighting, killed
        in ongoing, killed in fighting, killed ongoing fighting, in
        ongoing fighting}.
    """
    if n > len(lst) or k > len(lst):
        raise 'Invalid values for n:{0} or k:{1}'.format(n, k) 
    #Optimization for normal n-grams (0-skip-n-grams)
    if(k==0):
        return zip(*[lst[i:] for i in range(n)])
    else:
        idx_token_dict = dict(map(lambda el: reversed(el), enumerate(lst)))
        n_grams = combinations(lst, n)
        return filter(lambda ngram: is_valid_k_skip(map(lambda el: idx_token_dict[el], ngram), k), n_grams)

if(__name__== '__main__'):
    from sys import argv
    if(len(argv) != 4):
        print 'Usage'
        print 'python skip_gram_generator.py <token_list> <k (no.of skips)> <n (n=2 => bigram, n=3 => trigram etc.)>'
    else:
        print generate_k_skip_n_gram(ast.literal_eval(argv[1]), int(argv[2]), int(argv[3]))