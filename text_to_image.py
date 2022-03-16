from dataclasses import dataclass, field
from typing import Tuple
from PIL import Image, ImageDraw, ImageFont
# 1. property 작성 
# 2. Dataclass 로 작성 (V)
# 3. 바꾸는 함수 작성 (V)
# 4. 외부 인자 args 로 바꾸기
# 5. 인자에 무슨 값인지 명시하기 Listing (V)
@dataclass
class TextParameters:
    font: str
    font_size: int
    font_color: Tuple[int, int, int] = (0, 0, 0)
    bg_color: Tuple[int, int, int] = (255, 255, 255)
    text_position: Tuple[int, int] = (0, 0)
    # block_size: int = 2

# text 변수는 계속 바뀌어야 한다. 따라서 getter setter 필요.
@dataclass
class TextImage:
    text: str
    _text: str = field(init=False)
    parameters: TextParameters
    image: Image
    size: Tuple[int, int]
   
    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, text: str) -> None:
        self._text = text
   
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
    draw.text(params.offsets,
              text,
              font=ImageFont.truetype(params.font, params.font_size),
              fill=params.font_color)
    return TextImage(text= text, parameters= params, image = image, size= image.size)


    
def match() -> None:
    pass

def calculate_simularity(self, text_image, image) -> float:
    pass