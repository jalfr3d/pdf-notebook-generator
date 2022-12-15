from fpdf import FPDF
import pandas as pd

# orientation P portrait or L landscape
pdf = FPDF(orientation="P", unit="mm", format="A4")

# to avoid breaking lines
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
    # set the header
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # w: width h: height ln: break line border=1 add black line in cell align: L left R right
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    for y in range(20, 298, 10):
        # x1 y1 and x2 y2 coord of line
        pdf.line(10, y, 200, y)

    # set the footer break line in position 265 mm is the footer of the page
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # the -1 is to match the right quantity of pages for each variable *see topics.csv
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set the footer for the blanks pages
        # 277 = h + 265
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output_lined.pdf")
