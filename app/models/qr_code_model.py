import PIL
import qrcode
from PIL import Image


def generate_qr_with_logo(data, logo_file):
    """
    Generates a stylized QR code with a centered transparent logo, fixed at 300x300 px.

    Args:
        data (str): The data to encode in the QR code.
        logo_file (FileStorage): The uploaded logo file.

    Returns:
        PIL.Image: The generated QR code image with the integrated logo.
    """
    # Target QR code size
    target_size = (300, 300)

    # Generate the QR code with high error correction
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate QR code image
    qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    # Resize QR code to 300x300 px
    qr_image = qr_image.resize(target_size, resample=Image.Resampling.LANCZOS)

    # Open and resize the logo
    logo = Image.open(logo_file).convert("RGBA")
    logo_size = (target_size[0] // 5, target_size[1] // 5)  # Logo is ~20% of QR size
    logo = logo.resize(logo_size, resample=Image.Resampling.LANCZOS)

    # Handle transparency: add a white background to the logo
    white_bg = Image.new("RGBA", logo.size, "white")
    white_bg.paste(logo, (0, 0), mask=logo)

    # Center the logo onto the QR code
    logo_position = (
        (qr_image.size[0] - logo_size[0]) // 2,
        (qr_image.size[1] - logo_size[1]) // 2,
    )
    qr_image.paste(white_bg, logo_position, mask=white_bg)

    return qr_image

def generate_qr_with_no_logo(data):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    return qr_image
