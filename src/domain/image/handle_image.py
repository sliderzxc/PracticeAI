from PIL import Image


class HandleImage:

    def __init__(self):
        pass

    @staticmethod
    def handle(image_path):
        image = Image.open(image_path)
        pixels = image.load()
        width, height = image.size

        red = 0
        green = 0
        blue = 0

        for x in range(width):
            for y in range(height):
                pixel = pixels[x, y]

                red += pixel[0]
                green += pixel[1]
                blue += pixel[2]

        red = int(red / (width * height))
        green = int(green / (width * height))
        blue = int(blue / (width * height))

        print('Color =', red, green, blue)

        return red, green, blue
