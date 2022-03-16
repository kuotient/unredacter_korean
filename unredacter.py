from text_to_image import TextParameters, generate_image_from_text
from pixelize import PixelizeParameters, pixelize_image
from compare_image import cosine_similarity, mean_squared_error, preprocessing
from resources.fonts import DemoFontPaths
from util.preprocessing import get_bounding_box, img_to_ary
from PIL import Image
# TODO: 텍스트 생성 클래스 만들기
from generate_text import TextGenerator

# ImageFont.truetype(str(DemoFontPaths.NanumGothic), 12)
THRESHOLD = 0.8

def unredactor(img_path: str = image_path,
               txt_params: TextParameters = text_parameters,
               pixel_params: PixelizeParameters = pixel_parameters):
    '''
    Something
    '''
    # 검열 된 이미지의 파일 경로를 받아옴
    original_image_path= img_path
    # PNG 는 Alpha Channel이 있으므로 Pillow 라이브러리를 통해 이미지를 불러오면서 RGB 값으로 바꿈
    original_image = Image.open(original_image_path).convert('RGB')
    # 검열 이미지를 numpy array로 변환
    # original_image = np.array(original_image) #뭔가.... 이런 식으로

    # 완성형(2300글자 내외)/ 전체 한글(11000글자 내외), 숫자, 특수기호에 대한 옵션이 포함 된 텍스트에 대한 클래스 생성
    # TODO: 한글 목록에 대한 파일이나 리스트 만들기
    text_generator = TextGenerator(options='complete')

    # 완성 텍스트를 위한 변수 선언
    saved_text: str = ''
    isFirst = True
    while():
        # generate_text 함수로 텍스트를 부를 때마다 다음 한글과 텍스트의 경계선을 계산하는
        # 함수를 만들고 이걸로 텍스트를 생성
        if isFirst:
            it_text = text_generator.get_text()
            # 검열 이미지에서 픽셀 시작 영역을 추출
            original_bbox = get_bounding_box(original_image)
            
        # 이전에 맞춘 텍스트에 생성된 텍스트를 결합
        try:
            text = saved_text + next(it_text)
        except StopIteration:
            print("완성된 텍스트를 모두 불러왔습니다.")      
        # 텍스트를 이미지로 변환
        text_image = generate_image_from_text(text, txt_params)
        # 텍스트 이미지에서 텍스트 영역을 추출
        text_bbox = get_bounding_box(text_image)

        # 검열 이미지를 경계선(픽셀 시작지점, 텍스트 끝 지점)에 맞게 자름
        original_image = original_image.crop(original_bbox[0],
                                             original_bbox[1],
                                             text_bbox[2],
                                             original_bbox[3]) #아마도 이렇게
        # 이미지를 픽셀화하는 함수를 호출하여 픽셀화된 이미지를 받아옴
        pixelized_image = pixelize_image(text_image, pixel_params)
        # 비교하기 전에 이미지를 전처리
        text_array = img_to_ary(pixelized_image)
        original_array = img_to_ary(original_image)
        # 이미지 비교
        score = cosine_similarity(original_array, text_array)
        # or
        # score = mean_squared_error(original_image, preprocessed_image)
        # or...
        # score = ImageChops.difference(original_image, preprocessed_image)

        # 기준 점수를 넘으면 성공 글자와 다음 글자의 위치를 저장하고 다음 글자로 넘어갈 수 있게 체크
        if score > THRESHOLD:
            saved_text += text
            isFirst = False
            # 마지막 글자를 찾았으면 종료
            if text_bbox[2] >= original_bbox[2]:
                break

    return saved_text, score

if __name__ == '__main__':
    IMAGE_PATH = './resources/images/test_image.png'
    text_parameters: TextParameters = TextParameters(font=DemoFontPaths.NanumGothic,
                                                     font_size=12,
                                                     font_color=(255, 255, 255),
                                                     bg_color=(0, 0, 0),
                                                     text_position=(0, 0))
    
    pixel_parameters: PixelizeParameters = PixelizeParameters(block_size=3)
    result, score = unredactor(IMAGE_PATH, text_parameters, pixel_parameters)
    print(result, score)