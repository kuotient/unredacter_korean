from dataclasses import dataclass
from util.text_to_image import TextImage, TextParameters

@dataclass    
class PixelizeParameters():
    '''
    Parameters for pixelizing an image.
    '''
    block_size: int = 2

@dataclass
class PixelizedImage(TextImage):
    '''
    Class for pixelized images.
    '''
    parameters: PixelizeParameters

def pixelize_image(text_image: TextImage, params: PixelizeParameters) -> PixelizedImage:
    '''
    Pixelates an image by a given block size.
    Args:
        image: Image to pixelate.
        block_size: Size of the block to use when pixelating.
    Returns:
        Pixelated image.
    '''
    image = text_image.image
    width, height = text_image.size
    block_size = params.block_size
    cropped_width = width - (width % block_size)
    cropped_height = height - (height % block_size)
    pix = image.load()
    # TODO: Use this array to compare each images. pix_ary = []
    for y in range(0, cropped_height, block_size):
        for x in range(0, cropped_width, block_size):
            red, green, blue = 0, 0, 0
            for y1 in range(y, y+block_size):
                for x1 in range(x, x+block_size):
                    red += pix[x1, y1][0]
                    green += pix[x1, y1][1]
                    blue += pix[x1, y1][2]
            red = red/block_size**2
            green = green/block_size**2
            blue = blue/block_size**2
            for y1 in range(y, y+block_size):
                for x1 in range(x, x+block_size):
                    pix[x1, y1] = (int(red), int(green), int(blue))
    return PixelizedImage(text= text_image.text, parameters= params, image= image, size= image.size)