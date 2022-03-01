from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (70, 30), color='grey')
# image.show()
draw = ImageDraw.Draw(image)
draw.text((0, 0), "안녕하세요", font=ImageFont.truetype("data/fonts/NanumBarunGothic.ttf", 12), fill=(0,0,0))
image.show()