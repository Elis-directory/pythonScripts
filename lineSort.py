import sys
from pdfminer.high_level import extract_text
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def extract_text_from_pdf(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return ""

def sort_lines_lexicographically(text):
    lines = text.splitlines()
    lines = [line.strip() for line in lines if line.strip()]
    return sorted(lines)

def save_to_pdf(sorted_lines, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    y = height - 40  # Start 40 units from the top
    for line in sorted_lines:
        if y < 40:  # Add a new page if we're too close to the bottom
            c.showPage()
            y = height - 40
        c.drawString(40, y, line)
        y -= 14  # Move down 14 units for the next line
    c.save()

def main(pdf_paths):
    if len(pdf_paths) > 5:
        print("You can only process up to 5 PDF files at a time.")
        return

    all_text = ""
    for pdf_path in pdf_paths:
        if not os.path.isfile(pdf_path):
            print(f"File not found: {pdf_path}")
            continue

        text = extract_text_from_pdf(pdf_path)
        all_text += text

    sorted_lines = sort_lines_lexicographically(all_text)
    
    # Print sorted lines to the console
    for line in sorted_lines:
        print(line)
    
    # Save sorted lines to a PDF file
    output_pdf = "sorted_output.pdf"
    save_to_pdf(sorted_lines, output_pdf)
    print(f"Sorted lines saved to {output_pdf}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <pdf1> <pdf2> ... <pdf5>")
    else:
        main(sys.argv[1:])
