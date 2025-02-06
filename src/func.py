import pymupdf

doc = pymupdf.open("230507866v2.pdf")
text = ""
for page in doc:
    text += page.get_text()

print(text)