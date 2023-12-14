from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, Spacer, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

def modifiedInput(question, default_answer, answer_type):
    answer = input(f"{question} ({default_answer}) ").lower()
    if answer == "":
        return answer_type(default_answer)
    return answer_type(answer)

class Margin:
    def __init__(self, top = 0.75, bottom = 0.75, left = 0.5, right = 0.5):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

    def get(self):
        return f"{self.top} {self.bottom} {self.left} {self.right}"
    
    def input(self):
        print("This utility will walk you through to set the margins.", end="\n\n")
        print("Press ^C at any time to quit.")
        top = modifiedInput("margin top:", 0.75, float)
        bottom = modifiedInput("margin bottom:", 0.75, float)
        left = modifiedInput("margin left:", 0.5, float)
        right = modifiedInput("margin right:", 0.5, float)
        print(f"The margin will be {self.get()}", end="\n\n")
        confirmation = modifiedInput("Is this OK?", "yes", str)
        if confirmation == "yes":
            self.top = top
            self.bottom = bottom
            self.left = left
            self.right = right
        return self


def create_pdf(margins):
    doc = BaseDocTemplate("cv.pdf",
    pagesize=A4,
    topMargin=margins.top * inch,
    bottomMargin=margins.bottom * inch,
    leftMargin=margins.left * inch,
    rightMargin=margins.right * inch,
    )

    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
    
    Elements = []
    Elements.append(Paragraph("Syafiq Ziyadul Arifin"))
    
    doc.addPageTemplates([PageTemplate(id="OneCol", frames=frame)])
    doc.build(Elements)

if __name__ == "__main__":
    margin = Margin()
    create_pdf(margin)