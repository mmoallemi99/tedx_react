from PIL import Image
from io import BytesIO


def test_image_generator():
    tmp_file = BytesIO(b'fake file stream for test')
    image = Image.new('RGB', (10, 10))
    image = image.save(tmp_file, format='png')
    return image
