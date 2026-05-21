from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(80, 80, 80)
        # Changed em dash (—) to normal hyphen (-) to avoid Unicode error
        self.cell(0, 8, "TechCorp Inc. - Internal Document", align="L")
        self.ln(2)
        self.set_draw_color(200, 200, 200)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()} | Confidential", align="C")

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(30, 80, 160)
        self.ln(4)
        self.cell(0, 8, title, ln=True)
        self.set_draw_color(30, 80, 160)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)
        self.set_text_color(0, 0, 0)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(50, 50, 50)
        self.ln(3)
        self.cell(0, 7, title, ln=True)
        self.set_text_color(0, 0, 0)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        self.cell(8)
        self.multi_cell(0, 6, f"- {text}")


# ── PDF 1: Employee Handbook ───────────────────────────────
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(30, 80, 160)
pdf.ln(8)
pdf.cell(0, 12, "TechCorp Employee Handbook", align="C", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 7, "Version 4.0  |  Effective January 2024", align="C", ln=True)
pdf.ln(10)

pdf.chapter_title("1. Welcome to TechCorp")
pdf.body_text("TechCorp Inc. was founded in 2008 with a mission to deliver enterprise-grade software solutions...")
pdf.body_text("We believe in a culture of transparency, continuous learning, and mutual respect...")

pdf.chapter_title("2. Code of Conduct")
pdf.section_title("2.1 Professional Behaviour")
pdf.body_text("All employees are expected to maintain the highest standards of professional conduct...")
# (rest of sections same as before)

# Save Employee Handbook PDF to your Windows path
pdf.output(r"C:\Users\Pavani\rag-project\data\raw\pdfs\employee_handbook.pdf")
print("Created employee_handbook.pdf")


# ── PDF 2: AI Strategy Document ─────────────────────────────
pdf2 = PDF()
pdf2.set_auto_page_break(auto=True, margin=15)
pdf2.add_page()

pdf2.set_font("Helvetica", "B", 18)
pdf2.set_text_color(30, 80, 160)
pdf2.ln(8)
pdf2.cell(0, 12, "TechCorp AI Strategy 2024-2026", align="C", ln=True)
pdf2.set_font("Helvetica", "", 11)
pdf2.set_text_color(100, 100, 100)
pdf2.cell(0, 7, "Chief Technology Office  |  March 2024  |  Confidential", align="C", ln=True)
pdf2.ln(10)

pdf2.chapter_title("Executive Summary")
pdf2.body_text("This document sets out TechCorp's artificial intelligence strategy for the period 2024 to 2026...")
# (rest of sections same as before)

# Save AI Strategy PDF to your Windows path
pdf2.output(r"C:\Users\Pavani\rag-project\data\raw\pdfs\ai_strategy_2024.pdf")
print("Created ai_strategy_2024.pdf")

print("All PDFs generated successfully.")
