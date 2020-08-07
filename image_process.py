from PIL import Image

def post_thumbnail():
    img = Image.open('./static/img/home.jpg')
    resized = img.resize((700,300))
    resized.save('homes.jpg')

post_thumbnail()