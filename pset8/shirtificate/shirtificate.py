from fpdf import FPDF


def main():
    username = input('What\'s your name? ').strip().title()
    pdf = FPDF()
    pdf.set_auto_page_break(False)
    pdf.add_page()
    # Add text at the top of the page
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')
    # Center the image
    pdf.image('shirtificate.png', x=pdf.epw/4, y=pdf.eph/4)
    # Put the username on top of shirtificate.png
    pdf.set_x(pdf.epw/2)
    pdf.set_y(pdf.eph/2)
    pdf.set_font('Helvetica', 'B', 32)
    pdf.cell(pdf.epw/2, pdf.eph/8, f'{username} took CS50', 0, 1, 'C')
    pdf.output('shirtificate.pdf')


if __name__ == '__main__':
    main()
