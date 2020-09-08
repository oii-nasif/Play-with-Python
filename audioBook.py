# pip install pyttsx3
# pip install PyPDF2

import pyttsx3
import PyPDF2

book = open('Deep Learning.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(8)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()

