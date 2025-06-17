from fpdf import FPDF
import tempfile
import unicodedata

def sanitize_text(text):
    return unicodedata.normalize('NFKC', text).encode("ascii", "ignore").decode("ascii")

def generate_cover_letter_pdf(text, filename="cover_letter.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    clean_text = sanitize_text(text)
    for line in clean_text.split("\n"):
        pdf.multi_cell(0, 10, line.strip())

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_file.name)
    return temp_file.name