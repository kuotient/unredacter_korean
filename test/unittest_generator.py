from generate_text import TextGenerator
import unittest

class GenerateTextImages(unittest.TestCase):
    '''
    unittest for generate_text.py
    '''
    def test_generate_text(self):
        text_generator = TextGenerator()

        it_text = iter(text_generator.get_text())
        korean_list= ['가', '나', '다', '라', '마', '바', '사',
                        '아', '자', '차', '카', '타', '파', '하', '에러']
        for i in range(15):
            try:
                text = next(it_text)
                print(text)
                self.assertEqual(text, korean_list[i])
            except StopIteration:
                print("텍스트 완료")
            
            
if __name__ == '__main__':
    unittest.main()