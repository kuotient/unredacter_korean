from PIL import Image, ImageDraw, ImageFont, ImageOps
import time

# constants
BLOCK_SIZE = 3
OFFSET_X = 0
OFFSET_Y = 0


test_image = Image.new('RGB', (150, 30), color='white')
# image.show()
draw = ImageDraw.Draw(test_image)
draw.text((0, 0), "산과 물이 마르고 닳도록", font=ImageFont.truetype("data/fonts/NanumBarunGothic.ttf", 12), fill=(0,0,0))
# image.show()

#invert, bbox, crop
def crop_image(image):
    '''
    Crops an image to remove the white space around the text.
    Args:
        image: Image to crop.
    Returns:
        Cropped image.
    '''
    image = ImageOps.invert(image)
    image = image.crop(image.getbbox())
    image = ImageOps.invert(image)

    return image


#pixelate
# TODO: Use more functions
def pixelate_image(image, block_size):
    '''
    Pixelates an image by a given block size.
    Args:
        image: Image to pixelate.
        block_size: Size of the block to use when pixelating.
    Returns:
        Pixelated image.
    '''
    width, height = image.size
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
    return image

def preprocess_image(image):
    '''
    Preprocesses an image by applying filters and other manipulations.
    Args:
        image: Image to preprocess.
    Returns:`
        Preprocessed image.
    '''
    image = crop_image(image)
    image = pixelate_image(image, BLOCK_SIZE)
    return image

start = time.time()
processed_image = preprocess_image(test_image)
end = time.time()
print(end - start)
# print(type(pixelated_image))
# pixelated_image = Image.fromarray(pixelated_image)
processed_image.show()


