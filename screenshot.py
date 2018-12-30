from PIL import Image, ImageGrab
image = ImageGrab.grabclipboard()
name = input("Name the image please: ")
if isinstance(image, Image.Image):
    image.save(name+'.jpg')