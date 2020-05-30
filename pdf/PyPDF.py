import fitz

# pdf_document = "muzika.pdf"
# doc = fitz.open(pdf_document)
# print("Исходный документ: ", doc)
# print("\nКоличество страниц: %i\n\n------------------\n\n" % doc.pageCount)
# print(doc.metadata)
#
# for current_page in range(5,6):
#     page = doc.loadPage(current_page)
#     page_text = page.getText()
#     print("Стр. ", current_page+1, "\n\nСодержание;\n")
#     print(page_text)


from PyPDF2 import PdfFileReader
#
# pdf_document = "Sobitiya.pdf"
# with open(pdf_document, "rb") as f:
#    pdf = PdfFileReader(f)
#    info = pdf.getDocumentInfo()
#    pages = pdf.getNumPages()
#    print (info)
#    print ("number of pages: %i" % pages)
#    page1 = pdf.getPage(0)
#    print(page1)
#    print(page1.extractText())


pgs = open('muzika.pdf', 'rb')
read_pdf = PdfFileReader(pgs)
number = read_pdf.getNumPages()
page = read_pdf.getPage(6)
page_content = page.extractText()
print(page_content.encode('utf-8'))
