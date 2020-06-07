from PIL import Image
import imagehash


class ImgTools():
    
    def get_dhash(self, img_path):
        image = Image.open(img_path)
        hash = str(imagehash.dhash(image))
        return hash