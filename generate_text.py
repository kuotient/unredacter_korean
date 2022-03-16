from typing import List
import pickle

class TextGenerator():
    '''
    Generates a Korean text.
    '''
    def __init__(self, options: str = 'complete'):
        self.options: str = options
        self.korean_list: List[str] = ['가', '나', '다', '라', '마', '바', '사',
                                       '아', '자', '차', '카', '타', '파', '하']

        def get_korean_list():
            with open('resources/korean_frequency/complete_korean.pickle', 'rb') as f:
                korean_list = pickle.load(f)
            return korean_list
  
        self.korean_list2 = get_korean_list()

    # Use yield. Was it worth?
    def get_text(self):
        yield from self.korean_list

text_g = TextGenerator()