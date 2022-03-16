from PIL import Image, ImageOps
from typing import Tuple
import numpy as np
# 텍스트의 경계선을 나눌 때, 왼쪽은 픽셀화 된 텍스트의 경계를 기준으로,
# 오른쪽은 원본 텍스트의 경계를 기준으로 한다.
# 왼쪽의 시작을 고민해 봤는데, 결국 이건 offset 이니까.... 일단 생각 안하고 진행하기.

def img_to_ary(image):
    '''
    Preprocesses an image.
    Returns a preprocessed image.
    '''
    return np.array(image).flatten()/255

def get_bounding_box(image: Image) -> Tuple[int, int, int, int]:
    '''
    Gets the bounding box of an image.
    Args:
        image: Image to get the bounding box of.
    Returns:
        Bounding box of the image.
    '''
    image = ImageOps.invert(image)
    bbox = image.getbbox()
    return bbox
    
def crop_image(image: Image = None,
               bounding_box: Tuple[int, int, int, int] = None):
    '''
    Crops an image to the bounding box.
    Args:
        image: Image to crop.
    Returns:
        Cropped image.
    '''
    pass
    