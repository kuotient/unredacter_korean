from numpy import dot
from numpy.linalg import norm
import numpy as np
from scipy.spatial import distance

import time

# TODO: Calculate time difference between similarity functions
# Origial Image 를 비교할 때, 캐싱을 해둘 수 있을것 같은데?
# 돌아가면서 텍스트를 비교하지만, 원본 이미지에 대한 norm은 미리 계산된 값을 쓰는게 좋을것 같음.

def preprocessing(image):
    '''
    Preprocesses an image.
    Returns a preprocessed image.
    '''
    return np.array(image).flatten()/255

# IMAGE_ARY1 = preprocessing([(1,2,3), (4,5,6), (7,8,9)])
# IMAGE_ARY2 = preprocessing([(4,5,6), (4,5,6), (7,8,9)])
IMAGE_ARY1 = np.random.randn(1000,300,3).flatten()
IMAGE_ARY2 = np.random.randn(1000,300,3).flatten()

def cosine_similarity(image1, image2):
    '''
    Calculates the cosine similarity between two images.
    Returns a value between 0 and 1.
    '''
    # Maybe we can use...
    # 1. The scipy.spatial.distance.cosine function = Result: Take 0.96s
    #    Cosine Similarity = -(Cosine Distance -1)
    # 2. The numpy.linalg.norm function and the numpy.dot function
    # Numpy is faster than scipy
    # image1 = np.array(image1).flatten()/255
    # image2 = np.array(image2).flatten()/255

    return dot(image1, image2) / (norm(image1) * norm(image2))
    # return -(distance.cosine(image1, image2) - 1)

def ssim(image1, image2):
    '''
    Calculates the structural similarity between two images.
    Returns a value between 0 and 1.
    '''

    return ssim(image1, image2)

def mean_squared_error(image1, image2):
    '''
    Calculates the mean squared error between two images.
    '''

    return np.square(np.subtract(image1, image2)).mean()

start_time = time.time()
result = cosine_similarity(IMAGE_ARY1, IMAGE_ARY2)
end_time = time.time()
print(result)
print(end_time - start_time)

start_time = time.time()
result = mean_squared_error(IMAGE_ARY1, IMAGE_ARY2)
end_time = time.time()
print(result)
print(end_time - start_time)
