class open:
    def __init__(self):
        PathOfPDF = askopenfile()
        self.PDFFILE= PathOfPDF.name
        print(PDFFILE)

book = open(self.PDFFILE, 'rb')