from flask import Flask, render_template, request, make_response
from flask.ext.sqlalchemy import SQLAlchemy
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode.eanbc import Ean13BarcodeWidget
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from tempfile import NamedTemporaryFile

app = Flask(__name__)
app.config.from_object('config')

def generatePdf(description,upc,pages):
    tmpFile = NamedTemporaryFile(delete=False).name
    c=canvas.Canvas(tmpFile,pagesize=letter)
    count = 0
    page = 1

    products = list()
    for i in range(30*pages):
        products.append({"upc":upc, "description":description})

    marginTop = 8.8 * mm
    marginLeft = 4 * mm
    labelHeight = 25.5 * mm
    labelWidth = 67 * mm


    # Assume 10dx5a labels for now.
    finish = False
    while not finish:
        for i in reversed(range(10)):
            for j in range(3):
                try:
                    item = products[count]
                    print item["description"]
                    count = count + 1
                    x = marginLeft + (j*labelWidth)
                    y = marginTop + (i*labelHeight)
                    c.setFillColorCMYK(0,0,0,1)
                    c.setFont("Helvetica",12)
                    c.drawString(x + (10 * mm), y + (21 * mm), item["description"].upper())
                    drawing = Drawing()
                    barcode = Ean13BarcodeWidget()
                    barcode.value = str(int(item["upc"])).zfill(12)
                    barcode.barHeight = 12 * mm
                    barcode.barWidth = 0.95
                    barcode.fontSize = 6
                    drawing.add(barcode)
                    drawing.drawOn(c,x + (10 * mm), y + (8 * mm))
                except:
                    finish = True
        c.showPage()

    c.save()
    response = make_response(open(tmpFile).read())
    response.headers["Content-type"] = "application/pdf"
    return response

@app.route('/',methods=["POST","GET"])
def index():
    if request.method == 'POST':
        upc = int(request.form["upc"][:12])
        pages = int(request.form["pages"])
        description = request.form["description"].strip().upper()
        return generatePdf(description,upc,pages)
    else:
        return render_template('base.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

