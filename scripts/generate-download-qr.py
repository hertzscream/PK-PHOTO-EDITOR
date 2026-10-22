"""Generate and independently decode the static APK-download QR.
Development dependencies: qrcode[pil]==8.2 and zxing-cpp==2.3.0.
The website itself has no QR service or runtime dependency.
"""
from pathlib import Path
import qrcode
import zxingcpp
from PIL import Image

URL = 'https://github.com/hertzscream/PK-PHOTO-EDITOR/releases/latest/download/PK-PHOTO-EDITOR.apk'
OUTPUT = Path(__file__).resolve().parents[1] / 'docs/assets/download-qr.png'
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
qr.add_data(URL)
qr.make(fit=True)
image = qr.make_image(fill_color='black', back_color='white').convert('RGB')
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
image.save(OUTPUT)
# Decode from the saved file with an independent implementation.
result = zxingcpp.read_barcode(Image.open(OUTPUT))
assert result is not None and result.text == URL, 'QR decoding did not match the APK URL'
# Also check the actual display sizes used by the responsive layout.
for size in (148, 192):
    scaled = image.resize((size, size), Image.Resampling.LANCZOS)
    result = zxingcpp.read_barcode(scaled)
    assert result is not None and result.text == URL, f'QR unreadable at {size}px'
print(f'QR verified: {image.width}x{image.height}; display sizes 148px and 192px; {URL}')