# pylint: disable=missing-module-docstring missing-class-docstring missing-function-docstring no-member
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Paragraph,
    Spacer,
    PageTemplate,
    HRFlowable,
)
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black


def modified_input(question, default_answer, answer_type):
    answer = input(f"{question} ({default_answer}) ").lower()
    if answer == "":
        return answer_type(default_answer)
    return answer_type(answer)


class Margin:
    def __init__(self, top=0.75, bottom=0.75, left=0.5, right=0.5):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

    def get(self):
        return f"{self.top} {self.bottom} {self.left} {self.right}"

    def input(self):
        print("This utility will walk you through to set the margins.", end="\n\n")
        print("Press ^C at any time to quit.")
        top = modified_input("margin top:", 0.75, float)
        bottom = modified_input("margin bottom:", 0.75, float)
        left = modified_input("margin left:", 0.5, float)
        right = modified_input("margin right:", 0.5, float)
        print(f"The margin will be {self.get()}", end="\n\n")
        confirmation = modified_input("Is this OK?", "yes", str)
        if confirmation == "yes":
            self.top = top
            self.bottom = bottom
            self.left = left
            self.right = right
        return self


def create_pdf(margins):
    doc = BaseDocTemplate(
        "cv.pdf",
        pagesize=A4,
        topMargin=margins.top * inch,
        bottomMargin=margins.bottom * inch,
        leftMargin=margins.left * inch,
        rightMargin=margins.right * inch,
    )

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CVTitle",
            fontName="Times-Bold",
            fontSize=12,
            leading=12 * 1.2,
            alignment=TA_CENTER,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVDescription",
            fontName="Times-Italic",
            fontSize=12,
            leading=12 * 1.2,
            firstLineIndent=0.5 * inch,
            alignment=TA_JUSTIFY,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVSegmentTitle",
            fontName="Times-Bold",
            fontSize=12,
            leading=12 * 1.2,
            alignment=TA_CENTER,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVNormal",
            fontName="Times-Roman",
            fontSize=12,
            leading=12 * 1.2,
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVBullet",
            fontName="Times-Roman",
            fontSize=12,
            leading=12 * 1.2,
            alignment=TA_JUSTIFY,
            leftIndent=0.25 * inch,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVBulletWithIndent",
            fontName="Times-Roman",
            fontSize=12,
            leading=12 * 1.2,
            alignment=TA_JUSTIFY,
            leftIndent=0.5 * inch,
        )
    )

    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")

    elements = []

    elements.append(Paragraph("Syafiq Ziyadul Arifin", style=styles["CVTitle"]))
    elements.append(
        Paragraph(
            "+6282123456789 | <u><a href='mailto:szarifin20041@gmail.com'>szarifin20041@gmail.com</a></u> | <u><a href='https://linkedin.com/in/syafiqza'>linkedin.com/in/syafiqza</a></u>",
            style=styles["CVTitle"],
        )
    )

    elements.append(Spacer(0, 12 * 1.2))

    elements.append(
        Paragraph(
            "Spanning web development, Android development, robotics, and IoT, my interests have led me to proficiency in programming languages such as C++, Python, Go, and JavaScript. Currently in my third year of studying Information System and Technology at the Bandung Institute of Technology.",
            style=styles["CVDescription"],
        )
    )

    elements.append(Spacer(0, 12 * 1.2))

    # Education
    elements.append(Paragraph("Education", style=styles["CVSegmentTitle"]))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=black))

    spacer = (
        doc.width
        - doc.leftMargin / 4
        - stringWidth("Bandung Institute of Technology", "Times-Bold", 12)
        - stringWidth("Bandung, Indonesia", "Times-Roman", 12)
    ) / stringWidth(" ", "Times-Roman", 12)
    elements.append(
        Paragraph(
            f"<b>Bandung Institute of Technology</b>{'&nbsp;' * int(spacer-1)}Bandung, Indonesia",
            style=styles["CVNormal"],
        )
    )
    elements.append(
        Paragraph(
            "Bachelor, Information System and Technology. <b>GPA (4.00/4.00)</b>",
            style=styles["CVNormal"],
        )
    )
    elements.append(
        Paragraph(
            f"\t<bullet bulletIndent='{0.25*inch}'>&#x25cf;</bullet>Ranked 5th in Kontes Robot Indonesia (KRI) 2023 Region 1 and reached the top 16 nationally in Kontes Robot Sepak Bola Indonesia (KRSBI) Beroda.",
            style=styles["CVBulletWithIndent"],
        )
    )

    elements.append(Spacer(0, 12 * 1.2))

    # Leaderships & Activities
    elements.append(
        Paragraph("Leaderships & Activities", style=styles["CVSegmentTitle"])
    )
    elements.append(HRFlowable(width="100%", thickness=0.5, color=black))

    spacer = (
        doc.width
        - doc.leftMargin / 4
        - stringWidth("GIM (Ganesha Interactive Media) ITB", "Times-Bold", 12)
        - stringWidth("Bandung, Indonesia", "Times-Roman", 12)
    ) / stringWidth(" ", "Times-Roman", 12)
    elements.append(
        Paragraph(
            f"<b>GIM (Ganesha Interactive Media) ITB</b>{'&nbsp;' * int(spacer-1)}Bandung, Indonesia",
            style=styles["CVNormal"],
        )
    )
    elements.append(Paragraph("Programming", style=styles["CVNormal"]))
    elements.append(
        Paragraph(
            f"\t<bullet bulletIndent='{0.25*inch}'>&#x25cf;</bullet>Created two games using Unity and Godot as the final project of the internship.",
            style=styles["CVBulletWithIndent"],
        )
    )

    elements.append(Spacer(0, 12 * 1.2))

    # Skills & Interests
    elements.append(Paragraph("Skills & Interests", style=styles["CVSegmentTitle"]))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=black))

    elements.append(
        Paragraph(
            "<b>Technical</b>: C, C++, Java, JavaScript, OpenCV, Python, ROS.",
            style=styles["CVNormal"],
        )
    )

    elements.append(Spacer(0, 12 * 1.2))

    # Certifications & Licenses
    elements.append(
        Paragraph("Certifications & Licenses", style=styles["CVSegmentTitle"])
    )
    elements.append(HRFlowable(width="100%", thickness=0.5, color=black))

    elements.append(
        Paragraph(
            "\t<bullet>&#x25cf;</bullet><b><u><a href='https://courses.opencv.org/certificates/f6704946effd41b081f5ee9ca4faca3e'>OpenCV Bootcamp</a></u></b>, OpenCV University &ndash; June 2023",
            style=styles["CVBullet"],
        )
    )

    doc.addPageTemplates([PageTemplate(id="OneCol", frames=frame)])
    doc.build(elements)


if __name__ == "__main__":
    margin = Margin()
    create_pdf(margin)
