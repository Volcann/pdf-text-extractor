# PDF Text Extractor

A simple and scalable tool to extract text from PDF files and save the output into `.txt` files.  
Built with **Python** and a lightweight CLI script for automation.

---

## 📂 Project Structure
```

pdf-text-extractor/
│── examples/                  # Sample PDF files
│── output/                    # Extracted text files (auto-created)
│── scripts/
│   └── run\_extractor.py       # Python script to extract text from a single PDF
│── run\_all.sh                 # Bash script to batch process all PDFs in examples/
│── README.md                  # Project documentation

````

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/pdf-text-extractor.git
   cd pdf-text-extractor

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows

   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### Extract from a Single PDF

```bash
python scripts/run_extractor.py "examples/sample.pdf"
```

This will generate a `.txt` file in the `output/` folder with the same name as the PDF.

---

### Extract from All PDFs in `examples/`

```bash
bash run_all.sh
```

This will process every `.pdf` file inside `examples/` and save results into `output/`.

---

## 📝 Example Output

If your input is:

```
examples/sample.pdf
```

Your output will be:

```
output/sample.txt
```

---

## 📌 Notes

* Works best with text-based PDFs (not scanned images).
* For scanned/image PDFs, consider integrating **OCR** (e.g., `pytesseract` + `pdf2image`).
* Modify `scripts/run_extractor.py` if you want custom formatting.

---

## ✨ To-Do

* [ ] Add OCR support for scanned PDFs
* [ ] Improve text formatting (paragraphs, tables, etc.)
* [ ] Add tests for batch extraction
