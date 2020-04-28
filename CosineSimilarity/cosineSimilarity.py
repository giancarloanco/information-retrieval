import numpy as np
import math

def cosine_similarity(vector_1, vector_2):
    if (len(vector_1) != len(vector_2)):
        return -1
    
    num_dimensions = len(vector_1)
    print(num_dimensions)

    accumulated_sum = 0
    accumulated_pow_vector1 = 0
    accumulated_pow_vector2 = 0

    for i in range (num_dimensions):
        print(i, vector_1[i], vector_2[i])
        accumulated_sum = accumulated_sum + (vector_1[i] * vector_2[i])
        accumulated_pow_vector1 = accumulated_pow_vector1 + (pow(vector_1[i], 2))
        accumulated_pow_vector2 = accumulated_pow_vector2 + (pow(vector_2[i], 2))

    return (accumulated_sum / (math.sqrt(accumulated_pow_vector1) * math.sqrt(accumulated_pow_vector2))) 

def cosine_similarity_numpy(vector_1, vector_2):
    if (len(vector_1) != len(vector_2)):
        return -1
    
    return (np.dot(vector_1, vector_2) / (np.linalg.norm(vector_1) * np.linalg.norm(vector_2)))

u = [2,3,1,4]
v = [2,3,1,4.1]

print('Mine:\t', cosine_similarity(u, v))
print('Numpy:\t', cosine_similarity_numpy(u, v))
    
    
        
