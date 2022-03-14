from statistics import mean
from text_to_image import TextParameters, TextImage, generate_image_from_text
from pixelize import PixelizeParameters, PixelizedImage, pixelize_image
from compare_image import cosine_similarity, mean_squared_error, preprocessing
from resources.fonts import DemoFontPaths
# TODO: 텍스트 생성 클래스 만들기
from generator import TextGenerator

# ImageFont.truetype(str(DemoFontPaths.NanumGothic), 12)
THRESHOLD = 0.8

def unredactor(img_path= image_path, txt_params= text_parameters, pixel_params= pixel_parameters):
    # 검열 된 이미지의 파일 경로를 받아옴
    original_image_path= img_path
    # 검열 이미지를 numpy array로 변환
    original_image = cv2.imread(original_image_path)
    original_image = np.array(original_image) #뭔가.... 이런 식으로
    
    # 완성형(2300글자 내외)/ 전체 한글(11000글자 내외), 숫자, 특수기호에 대한 옵션이 포함 된 텍스트에 대한 클래스 생성
    # TODO: 한글 목록에 대한 파일이나 리스트 만들기
    text_generator = TextGenerator(options='complete')
    
    # 완성 텍스트를 위한 변수 선언
    final_text: str = ''
    while():
        # generate_text 함수로 텍스트를 부를 때마다 다음 한글과 텍스트의 경계선을 계산하는
        # 함수를 만들고 이걸로 텍스트를 생성
        text, text_boundary_box = text_generator.generate_text(final_text)
        # 검열 이미지를 경계선에 맞게 자름
        original_image = original_image[text_boundary_box[0]:text_boundary_box[1],
                                        text_boundary_box[2]:text_boundary_box[3]] #아마도 이렇게
        # 텍스트를 이미지로 변환
        text_image = generate_image_from_text(text, txt_params)
        # 이미지를 픽셀화하는 함수를 호출하여 픽셀화된 이미지를 받아옴
        pixelized_image = pixelize_image(text_image, pixel_params)
        # 비교하기 전에 이미지를 전처리
        preprocessed_image = preprocessing(pixelized_image)
        # 이미지 비교
        score = cosine_similarity(original_image, preprocessed_image)
        # or
        # score = mean_squared_error(original_image, preprocessed_image)
        
        # 기준 점수를 넘으면 성공 글자와 다음 글자의 위치를 저장
        if score > THRESHOLD:
            final_text += text
        # 마지막 글자를 찾았으면 종료
        if text_boundary_box[1] == original_image.shape[0]:
            break
    
    return final_text, score

if __name__ == '__main__':
    image_path = './resources/images/test_image.png'
    text_parameters: TextParameters = TextParameters(font=DemoFontPaths.NanumGothic, 
                                                     font_size=12,
                                                     font_color=(255, 255, 255), 
                                                     bg_color=(0, 0, 0),
                                                     text_position=(0, 0))
    
    pixel_parameters: PixelizeParameters = PixelizeParameters(block_size=3)
    result, score = unredactor(image_path, text_parameters, pixel_parameters)
    print(result, score)