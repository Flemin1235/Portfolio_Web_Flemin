from pathlib import Path
from pypdf import PdfReader
pdf = Path(r'e:\MySpace\Personal\SHAILESH_CV_SHORT.pdf')
reader = PdfReader(str(pdf))
for idx, page in enumerate(reader.pages, 1):
    text = page.extract_text()
    print(f'--- PAGE {idx} ---')
    print(text or '[no text extracted]')
