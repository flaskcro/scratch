def vector_add(v,w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v,w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    return reduce(vector_add, vectors)
