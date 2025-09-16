import sys
import os

# add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pdf_extractor.extractor import PDFTextExtractor

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/run_extractor.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_file = f"{base_name}.txt"

    extractor = PDFTextExtractor(pdf_path)
    text = extractor.extract_text()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ Extracted text saved to {output_file}")
