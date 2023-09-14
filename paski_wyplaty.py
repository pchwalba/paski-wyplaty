import sys
import PyPDF2


def split(file):
    try:
        with open(file, 'rb') as pdf_file:
            read_pdf = PyPDF2.PdfFileReader(pdf_file)
            count = read_pdf.numPages
            for i in range(count):
                page = read_pdf.getPage(i)
                page_content = page.extractText()
                index_start = page_content.find("Pracownik:") + 11
                index_end = page_content.find("(", index_start, index_start + 20) - 1
                name = page_content[index_start:index_end].replace('\n',' ')
                password = page_content[page_content.find("PESEL:") + 8: page_content.find("PESEL:") + 19]

                write_pdf = PyPDF2.PdfFileWriter()
                write_pdf.addPage(page)
                write_pdf.encrypt(password)
                with open(name + ".pdf", "wb") as output_file:
                    write_pdf.write(output_file)

    except FileNotFoundError:
        print("Plik %s nie istnieje" % file)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Wprowadź nazwę paska zbiorczego który chcesz podzielić i zaszyfrować: ")
    split(filename)

