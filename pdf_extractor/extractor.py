import fitz  # PyMuPDF
from pathlib import Path
import pytesseract
from PIL import Image

class PDFTextExtractor:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def extract_text(self) -> str:
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        text_content = []
        with fitz.open(self.file_path) as pdf:
            for page in pdf:
                text = page.get_text("text")
                if text.strip():
                    text_content.append(text)
                else:
                    # OCR fallback
                    pix = page.get_pixmap()
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    ocr_text = pytesseract.image_to_string(img)
                    if ocr_text.strip():
                        text_content.append(ocr_text)

        return "\n".join(text_content)
