from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from cosineSimilarityProject import cosineSimilarity

import numpy as np

def initial_page(request):

    html_page = open("F:/Universidad/DatabasesTopics/CosineSimilarity/cosineSimilarityProject/cosineSimilarityProject/templates/index.html")

    html_template = Template(html_page.read())

    html_page.close()

    vector_a = [1,2,3]

    context_html = Context({"num_vectors": vector_a})

    initial_page = html_template.render(context_html)

    return HttpResponse(initial_page)

def cosine_similarity_page(request):
    return render(request, "index.html")

def calculate_similarity(request):
    num_vectors_req = int(request.GET["input_num_vectors"])
    index_central_vector_req = int(request.GET["input_index_central_vector"])
    
    list_vectors = []

    for i in range (0, (len(request.GET) - 2)):
        temp_vector = np.fromstring(request.GET["input_vector_"+str(i)], dtype=float, sep=',')
        list_vectors.append(temp_vector)

    if (num_vectors_req != len(list_vectors)):
        print("Error")

    index_nearest_vectors, value_nearest_vector, ordered_vectors, scores_vectors = cosineSimilarity.find_nearest_vector(index_central_vector_req, list_vectors)

    print('Index Nearest Vectors:\t', index_nearest_vectors)
    print('Value Nearest Vector:\t', value_nearest_vector)

    print('Vectors:')
    for i in range (len(index_nearest_vectors)):
        print(index_nearest_vectors[i], list_vectors[index_nearest_vectors[i]])

    print('Ordered Vectors:\n', ordered_vectors)

    results_vectors = []
    results_scores_vectors = []

    for i in range (len(ordered_vectors) - 1):
        results_vectors.append(list_vectors[ordered_vectors[i]])

    for i in range (len(scores_vectors) - 1):
        results_scores_vectors.append(scores_vectors[ordered_vectors[i]])

    

    return render(request, "results.html", {"central_vector": list_vectors[index_central_vector_req], "ordered_vectors": results_vectors, "scores_vectors": results_scores_vectors})