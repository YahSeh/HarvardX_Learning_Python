from fpdf import FPDF
from PIL import Image

class PDF():
    def __init__(self, name) :
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font('helvetica', 'B', 50)
        self._pdf.cell(0, 60, 'CS50 Shirtificate', new_x='LMARGIN', new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_auto_page_break(0)
        self._pdf.set_font('helvetica', 'B', 25)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.cell(0, -225, f'{name} took CS50', new_x='LMARGIN', new_y="NEXT", align='C')


    def save(self, name) :
        self._pdf.output(name)


name = input("What is your name? ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")
