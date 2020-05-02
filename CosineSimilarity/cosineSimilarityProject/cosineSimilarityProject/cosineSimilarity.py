import numpy as np
import math

def cosine_similarity(vector_1, vector_2):
    if (len(vector_1) != len(vector_2)):
        return -1
    
    num_dimensions = len(vector_1)
    #print(num_dimensions)

    accumulated_sum = 0
    accumulated_pow_vector1 = 0
    accumulated_pow_vector2 = 0

    for i in range (num_dimensions):
        #print(i, vector_1[i], vector_2[i])
        accumulated_sum = accumulated_sum + (vector_1[i] * vector_2[i])
        accumulated_pow_vector1 = accumulated_pow_vector1 + (pow(vector_1[i], 2))
        accumulated_pow_vector2 = accumulated_pow_vector2 + (pow(vector_2[i], 2))

    return (accumulated_sum / (math.sqrt(accumulated_pow_vector1) * math.sqrt(accumulated_pow_vector2))) 

def cosine_similarity_numpy(vector_1, vector_2):
    if (len(vector_1) != len(vector_2)):
        return -1
    
    return (np.dot(vector_1, vector_2) / (np.linalg.norm(vector_1) * np.linalg.norm(vector_2)))

def find_nearest_vector(index_central_vector, vectors):
    central_vector = vectors[index_central_vector]

    results = np.full((len(vectors), 2), -1, dtype='float64')

    for i in range (len(vectors)):
        if (i != index_central_vector):
            results[i][0] = cosine_similarity(central_vector, vectors[i])
            results[i][1] = i

    print('Results Vector:\n', results)

    index_nearest_vectors = np.where(results[:,0] == np.amax(results[:,0]))[0]
    index_nearest_vectors = np.delete(index_nearest_vectors, np.where(index_nearest_vectors == index_central_vector))

    output_list = np.argsort(results[:,0]) #np.sort(results, axis=0) #np.argsort(results[:,0]) 
    output_list = output_list[::-1]
    
    return index_nearest_vectors, np.amax(results[:,0]), output_list, results[:,0]


u = [2,3,1,4]
v = [2,3,1,4.1]

print('Mine:\t', cosine_similarity(u, v))
print('Numpy:\t', cosine_similarity_numpy(u, v))

list_vectors = [[1, 2, 3], [1, 2, 4], [1, 2, 5]]
    
index_nearest_vectors, value_nearest_vector, ordered_vectors, scores_vectors = find_nearest_vector(0, list_vectors)

print('Index Nearest Vectors:\t', index_nearest_vectors)
print('Value Nearest Vector:\t', value_nearest_vector)

print('Vectors:')
for i in range (len(index_nearest_vectors)):
    print(index_nearest_vectors[i], list_vectors[index_nearest_vectors[i]])

print('Ordered Vectors:\n', ordered_vectors)
