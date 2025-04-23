import csv
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

# Step 1: Create the CSV file
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 22, "Chicago"]
]

filename = "data.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"{filename} created successfully.")

# Step 2: Convert CSV to Readable PDF
df = pd.read_csv("data.csv")

pdf_filename = "data.pdf"
c = canvas.Canvas(pdf_filename, pagesize=letter)
width, height = letter

# Convert dataframe to a list (including headers)
data_list = [df.columns.tolist()] + df.values.tolist()

# Create a table
table = Table(data_list)

# Add style to the table
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align text
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header bold
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),  # Padding for header
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Background color for data rows
    ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Grid lines
])

table.setStyle(style)

# Draw the table on the PDF
table.wrapOn(c, width, height)
table.drawOn(c, 50, height - 100)

c.save()
print(f"PDF '{pdf_filename}' created successfully.")
