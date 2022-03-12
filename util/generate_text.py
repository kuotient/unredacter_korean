from abc import ABC, abstractmethod

class TextGenerator(ABC):
    '''
    Abstract class for text generation
    '''
    @abstractmethod
    def generate(self):
        pass
    
class KoreanTextGenerator(TextGenerator):
    '''
    Generates a Korean text.
    '''
    def __init__(self, options: str):
        self.options = options
        
    def generate_text(self):
        return "안녕하세요"
    
class NumberTextGenerator(TextGenerator):
    '''
    Generates a number text.
    '''
    def generate(self):
        return "1"
    
