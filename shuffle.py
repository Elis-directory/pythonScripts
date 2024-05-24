import PyPDF2
import random


def shuffle_pdf(input_file, output_file):
    # Open the source PDF
    with open(input_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Create a list of page numbers and shuffle it
        page_numbers = list(range(num_pages))
        random.shuffle(page_numbers)

        # Create a PdfWriter object for the output file
        writer = PyPDF2.PdfWriter()

        # Add pages to the writer in shuffled order
        for page_number in page_numbers:
            writer.add_page(reader.pages[page_number])

        # Write the shuffled pages to the output PDF file
        with open(output_file, "wb") as output_file:
            writer.write(output_file)


# Example usage
input_path = "/Users/eliranchomoshe/Desktop/Finals/Practice_Tests/Chem_practice_test_new.pdf"
output_path = "/Users/eliranchomoshe/Desktop/Finals/Practice_Tests/Chem_practice_test_new2.pdf"
shuffle_pdf(input_path, output_path)
