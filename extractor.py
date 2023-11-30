import PyPDF2


def read_pdf_info():
    text = ""
    pdf_reader = PyPDF2.PdfReader("./input/edital_unicamp_2023.pdf")

    for page in pdf_reader.pages:
        text += page.extract_text().replace(" ", "").replace("\x00", "ti")

    return text


def writer(text):
    with open("output/data.txt", "w", encoding="utf-8") as f:
        f.write(text)
