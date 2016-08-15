from PIL import Image
im = Image.open('images/leo.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('images/leo.thumb.jpg', 'JPEG')