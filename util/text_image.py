from dataclasses import dataclass, field
from typing import List, Tuple
from PIL import Image, ImageDraw, ImageFont
# 1. property 작성
# 2. Dataclass 로 작성
# 3. 바꾸는 함수 작성
# 4. 외부 인자 args 로 바꾸기
# 5. 인자에 무슨 값인지 명시하기 Listing
@dataclass
class TextParameters:
    font: str
    font_size: int
    font_color: Tuple[int, int, int] = (0, 0, 0)
    bg_color: Tuple[int, int, int] = (255, 255, 255)
    offsets: Tuple[int, int] = (0, 0)
    # block_size: int = 2

@dataclass    
class PixelImageParameters(TextParameters):
    block_size: int = 2
    

@dataclass
class TextImage:
    text: str
    parameters: TextParameters
    image: Image
    size: Tuple[int, int]
    
@dataclass
class PixelizedImage(TextImage):
    parameters: PixelImageParameters
        

def generate_image_from_text(text: str, params: TextParameters) -> TextImage:
    '''
    Generates an image from a given text.
    Args:
        text: Text to generate an image from.
        params: Parameters to use when generating the image.
    Returns:
        Generated image, formed with TextImage Class.
    '''
    image: Image = Image.new('RGB', (150, 30), color= params.bg_color)
    draw = ImageDraw.Draw(image)
    draw.text(params.offsets, text, font=ImageFont.truetype(params.font, params.font_size), fill=params.font_color)
    return TextImage(text= text, parameters= params, image = image, size= image.size)

def pixelize_image(image: TextImage, params: PixelImageParameters) -> PixelizedImage:
    '''
    Pixelates an image by a given block size.
    Args:
        image: Image to pixelate.
        block_size: Size of the block to use when pixelating.
    Returns:
        Pixelated image.
    '''
    width, height = image.size
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
    return PixelizedImage(text= image.text, parameters= params, image= image, size= image.size)
    
def match() -> None:
    
    
    pass
    

def pixelize(self) -> None:
    pass

def calculate_simularity(self, text_image, image) -> float:
    pass