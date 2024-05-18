import PyPDF2
from typing import List

def extract_text_from_pdf(pdf_file: str) -> List[str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text

def clean_text(text_list: List[str]) -> str:
    # Join the text list into a single string
    text = ' '.join(text_list)

    # Replace multiple newlines and spaces with a single space
    text = text.replace('\n', ' ')
    text = ' '.join(text.split())

    return text

if __name__ == "__main__":
    extracted_text = extract_text_from_pdf("mypdf.pdf")
    cleaned_text = clean_text(extracted_text)
    print(cleaned_text)
