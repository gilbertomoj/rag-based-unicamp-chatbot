import PyPDF2


def read_pdf_info():
    pdf_reader = PyPDF2.PdfReader("./input/edital_unicamp_2023.pdf")
    text = ''.join(page.extract_text().replace(" ", "").replace("\x00", "ti") for page in pdf_reader.pages)
    with open("output/data.txt", "w", encoding="utf-8") as f:
        f.write(text)
