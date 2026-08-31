reader = PdfReader("doc4_travel_expense_policy.pdf")
pdf_text = ""

for rec in reader.pages:
    pdf_text += rec.extract_text()
