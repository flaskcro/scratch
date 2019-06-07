import math

def vector_add(v,w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v,w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(c,v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply( 1/n, vector_sum(vectors) )
    
def dot(v,w):
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v,w):
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    return magnitude(vector_subtract(v,w))


def mean(x):
    return sum(x) / len(x)

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        return (sorted_v[midpoint-1] + sorted_v[midpoint])/2
    
def quantile(v, p):
    p_index = int(p * len(v))
    return sorted(v)[p_index]

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]
 
def data_range(v):
    return max(v) - min(v)

def de_mean(x):
    x_mean = mean(x)
    return [x_i - x_mean for x_i in x]

def variance(x):
    n = len(x)
    deivaitions = de_mean(x)
    return sum_of_squares(deviations) / (n-1)

def standard_deviations(x):
    return math.sqrt(variance(x))

def interquantile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

def covariance(x,y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)

def correlations(x,y):
    stddev_x = standard_deviation(x)
    stddev_y = standard_deviation(y)
    if (stddev_x > 0 and stddev_y > 0):
        return covariance(stddev_x, stddev_y) / (stddev_x * stddev_y)
    else:
        return 0
