import math
from random import random

def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
    if x < 0: return 0
    elif x < 1 : return x
    else: return 1

def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (1 / sqrt_two_pi * sigma) * ( math.exp( -(x-mu)**2/2*sigma**2 ) )

def normal_cdf(x, mu=0, sigma=1):
    return ( 1+ math.erf((x-mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance = 0.00001):
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance = tolerance)
    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 1
    while hi_z - low_z > tolerance:
        mid_z = (hi_z + low_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_Z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_Z, mid_p
        else:
            break
    return mid_z


def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

def normal_probablity_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

def normal_probablity_below(x, mu=0, sigma=1):
    return normal_cdf(x, mu=0, sigma=1)

def normal_probablity_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

def normal_probablity_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probablity_between(lo, hi, mu, sigma)

def normal_upper_bound(probablity, mu=0, sigma=1):
    return inverse_normal_cdf(probablity, mu, sigma)

def normal_lower_bound(probablity, mu=0, sigma=1):
    return inverse_normal_cdf(1-probablity, mu, sigma)

def normal_two_slided_bound(probablity, mu=0, sigma=1):
    tail_probablity = ( 1- probablity) / 2
    upper_bound = normal_lower_bound(tail_probablity, mu, sigma)
    lower_bound = normal_upper_bound(tail_probablity, mu, sigma)
    return lower_bound, upper_bound

def two_sided_p_value(x, mu=0, sigma=1):
    if x > mu:
        return 2 * normal_probablity_above(x, mu, sigma)
    else:
        return 2 * normal_probablity_below(x, mu, sigma)

## for AB Test
def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1-p) / N) #N이 크기때문에 편의상 t분포가 아닌 정규분포를 이용
    return p, sigma

def ab_test_statistics(Na, na, Nb, nb): 
    #Na Number of A test users, na : Conversion counts of A test
    pA, sigmaA = estimated_parameters(Na, na)
    pB, sigmaB = estimated_parameters(Nb, nb)
    return (pB - pA) / math.sqrt(sigmaA ** 2 + sigmaB ** 2)
