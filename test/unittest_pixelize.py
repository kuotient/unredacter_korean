import unittest

from pixelize import PixelizeParameters
from pixelize import pixelize_image
from text_to_image import TextParameters, generate_image_from_text

text = '동해물과 백두산이'
font = 'data/fonts/NanumBarunGothic.ttf'
font_size = 12
bg_color = (255, 255, 255)
offsets = (0, 0)

text_parameters: TextParameters = TextParameters(
    font=font,
    font_size=font_size,
    bg_color=bg_color,
    offsets=offsets)

text_image = generate_image_from_text(text, text_parameters)
# text_image.image.show()


class GenerateTextImages(unittest.TestCase):
    '''
    pixelize 에 대한 유닛 테스트 케이스
    '''
    def test_pixelize_images(self):
        block_size: int = 3
        pixelize_parameters = PixelizeParameters(block_size=block_size)
        
        pixelized_image = pixelize_image(text_image, pixelize_parameters)
        pixelized_image.image.show()
    
if __name__ == '__main__':
    unittest.main()