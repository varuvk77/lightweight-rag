import os
import pymupdf4llm

os.makedirs("markdown", exist_ok=True)

pdf_path = "documents/LAB PROJECT LDICA.pdf"

markdown = pymupdf4llm.to_markdown(pdf_path)

with open("markdown/sample.md", "w", encoding="utf-8") as f:
    f.write(markdown)

print("PDF converted successfully!")
