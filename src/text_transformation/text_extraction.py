from pypdf import PdfReader


def read_all_pages(pdf_name):
    reader = PdfReader(pdf_name)
    page_count = reader.get_num_pages()
    text = ""
    for page in range(page_count):
        text += reader.pages[page].extract_text()
    return text


def read_pdf(pdf_name, page_no):  # TODO:Build multi-page reader fn.
    """
    Extracts text form pdf given of a specific page number and returns the text
    """
    reader = PdfReader(pdf_name)
    # print("Total page count : ", page_count)
    text = reader.pages[page_no].extract_text()
    return text


def write_to_text(input_text, filename):
    """
    Takes text and writes it into a file
    """

    with open(filename, "w") as f:
        f.write(input_text)


# text = read_all_pages("../../documents/AReviewOnDatabaseSecurity.pdf")
# print(text)
