from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib import colors
import os, sys


def generateCertificate( name, date, text):
    # these values were picked because of the canva site certificate
    PAGE_HEIGHT = 1414
    PAGE_WIDTH = 2000
    
    # Remove spaces from Name for saving pdf
    name = name.strip()
    strippedName = str(name).replace(" ", "")

    # pdf filename = certificates\StudentName-certificate-1.pdf
    fileName = os.path.join("certificates/", strippedName+"-certificate-1.pdf")  
    canvas = Canvas(fileName, (PAGE_WIDTH,PAGE_HEIGHT))

    # Draw Images
    canvas.drawImage('header.png',0,PAGE_HEIGHT-540,width=PAGE_WIDTH,height=540,preserveAspectRatio=True)
    canvas.drawImage('footer.png',0,-10,width=PAGE_WIDTH,height=364,preserveAspectRatio=True)

    # Student Name, check the length of the name and adjust size and location to fit on page
    text_len = canvas.stringWidth(name,"Times-Roman", 10)
    if text_len > 220:
        canvas.setFont("Times-Roman", 75)
        multiplier = (text_len/2*9.5)
    elif text_len > 190:
        canvas.setFont("Times-Roman", 90)
        multiplier = (text_len/2*9.5)
    elif text_len > 140: 
        canvas.setFont("Times-Roman", 105)
        multiplier = (text_len/2*10.5)
    else:
        canvas.setFont("Times-Roman", 128.4)
        multiplier = (text_len/2*13.5)
    
    # color matched from certificate from canva
    canvas.setFillColor(colors.HexColor("#4C96F1"))
    canvas.drawString(PAGE_WIDTH/2 - multiplier, PAGE_HEIGHT/2 + 70, str(name))

    # Adding Text, a little complicated to automatically wrap the text
    # Add to a Paragraph,
    # Add paragraph to a table
    # https://stackoverflow.com/questions/2121909/word-wrap-on-report-lab-pdf-table
    styleN1 = ParagraphStyle(
        name='index',
        fontName="Times-Roman",
        fontSize=42,
        # color matched from certificate from canva
        textColor=colors.HexColor("#9cb3C6"),
        leading=60,
        leftIndent=10
        #doesnt work
        #alignment='CENTER'
    )

    desc = Paragraph(text, styleN1)
    data= [[desc]]
    table = Table(data)
    table.setStyle(TableStyle([
                        #('INNERGRID', (0,0), (-1,-1), 0.25, colors.green),
                        #('BOX', (0,0), (0,0), 0.25, colors.red),
                        #('ALLIGN',(0,0),(-1,-1),'CENTER')
                        ]))
    table.wrapOn(canvas, PAGE_WIDTH -300, PAGE_HEIGHT)
    table.drawOn(canvas, 170 , PAGE_HEIGHT/2 - 250 )

    # Add Date
    canvas.setFont("Times-Roman", 40)
    # color matched from certificate from canva
    canvas.setFillColor(colors.HexColor("#737373"))
    canvas.drawString( PAGE_WIDTH/2 - 180, 330, str(date))
    # Save the PDF file
    canvas.save()