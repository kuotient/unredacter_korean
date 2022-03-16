import unittest

from text_to_image import TextParameters
from text_to_image import generate_image_from_text
#from params import TextImageParameters, PixelImageParameters


class GenerateTextImages(unittest.TestCase):
    '''
    image.py 에 대한 유닛 테스트 케이스
    '''
    def test_generate_text_images(self):
        # parameters
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
        text_image.image.show()
        self.assertEqual(text_image.text, text)


if __name__ == '__main__':
    unittest.main()