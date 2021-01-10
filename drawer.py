from PIL import Image

class Drawer:

    def draw(img, path):
        img = img.convert('RGB')
        output_image = img
        l = len(path)
        multiple = 255/l
        counter = 0
        for node in path:
            r = int(counter * multiple)
            counter += 1
            output_image.putpixel((node[1], node[0]), (0,r,255-r))
        
        output_image.save("images/output.png", "PNG")
        output_image.show()