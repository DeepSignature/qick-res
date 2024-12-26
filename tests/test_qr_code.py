import unittest
from app.models.qr_code_model import generate_qr_with_logo
from PIL import Image
import io

class TestQRGeneration(unittest.TestCase):
    def test_generate_qr_with_logo(self):
        # Test data
        data = "Hello, World!"
        logo_file = io.BytesIO()

        # Create a small test logo
        logo = Image.new('RGB', (100, 100), color=(255, 0, 0))
        logo.save(logo_file, format="PNG")
        logo_file.seek(0)

        # Generate the QR code
        qr_image = generate_qr_with_logo(data, logo_file)

        assert isinstance(qr_image, Image.Image)  # Ensure it returns an Image object
        assert qr_image.size == (300, 300)  # Default size of QR code with box_size=10 and border=4


if __name__ == '__main__':
    unittest.main()
